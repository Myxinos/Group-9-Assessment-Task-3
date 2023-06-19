import json
import time

from flask import render_template, Blueprint, request, session, flash, url_for, redirect
from flask_login import current_user
from App.controllers.common.utils import to_json
from App.models.models import db, Concert, Comment, User, Book
from App.models.forms import CommentForm, EventForm
from flask_login import login_required
from werkzeug.utils import secure_filename
import os
import platform
import datetime

index_event = Blueprint('index_event', __name__, )


@index_event.route('event/add.html', methods=['GET', 'POST'])
@login_required
def add():
    form = EventForm()
    return render_template('event/add.html', form=form)


@index_event.route('/event/save.html', methods=['POST'])
@login_required
def save():
    f = request.files['file']
    if f:
        filename = secure_filename(f.filename)
        file_date = str(time.time())
        runtime_dir = os.path.dirname(os.path.abspath(__file__))
        sys = platform.system()
        static_dir = ''
        if sys == "Windows":
            base_dir = runtime_dir.split('\App')
            static_dir = os.path.join(base_dir[0], 'App\\static\\uploads\\')
        else:
            base_dir = runtime_dir.split('/App')
            static_dir = os.path.join(base_dir[0], 'App/static/uploads/')
        f.save(os.path.join(static_dir, file_date + filename))
    try:
        form = EventForm()
        if form.validate_on_submit():
            obj = {
                'price': form.price.data,
                'eventImage': '/static/uploads/{}/{}'.format(file_date, filename),
                'eventName': form.eventName.data,
                'eventOrganizer': form.eventOrganizer.data,
                'category': form.category.data,
                'musician': form.musician.data,
                'tags': form.tags.data,
                'eventDate': form.eventDate.data.strftime('%m/%d/%Y'),
                'content': form.content.data,
                'startTime': form.startTime.data.strftime("%m/%d/%Y, %H:%M:%S"),
                'endTime': form.endTime.data.strftime("%m/%d/%Y, %H:%M:%S"),
                'timeZone': form.timeZone.data,
                'language': form.language.data,
                'locationType': form.locationType.data,
                'location': form.location.data
            }
            admin = Concert(obj)
            db.session.add(admin)
            db.session.commit()
            flash('event is created successfully', 'success')
            return redirect(url_for("index_index.index"))
    except Exception as e:
        print(f'Exception:{e}')
        flash('Something is wrong, please check', 'success')
        return redirect(url_for("index_event.add"))


@index_event.route('event/detail.html', methods=['GET', 'POST'])

def detail():
    id = request.args.get("id")
    info = Concert.query.filter(Concert.id == id).first()
    commentform = CommentForm()

    # get comments
    rows = Comment.query.filter(Comment.concert_id == id).all()
    comments = []
    for row in rows:
        item = to_json(row)
        item['addtime'] = time.strftime(
            '%Y-%m-%d %H:%M:%S', time.localtime(int(item['addtime'])))

        user = User.query.filter_by(id=item['user_id']).first()

        if user is not None:
            item['user'] = user.username
        comments.append(item)
    print(comments)
    return render_template('event/detail.html', **{'info': info, 'comments': comments, 'commentform': commentform})


@index_event.route('/event/saveComment', methods=['POST'])
@login_required
def comment():
    form = CommentForm()
    if form.validate_on_submit():
        concert_id = form.concert_id.data
        content = form.content.data
        user_id = current_user.id
        admin = Comment({'concert_id': concert_id,
                        'content': content, 'user_id': user_id})
        db.session.add(admin)
        db.session.commit()
        flash('comment success', 'success')
        return redirect('/index/event/detail.html?id={}'.format(concert_id))


@index_event.route('/event/book.html', methods=['POST'])
@login_required
def book():
    state = 0
    msg = "book error"

    user_info = session.get('user_info')

    if user_info is None:
        ret = {"state": state, "msg": "Please log in first before booking"}
        return json.dumps(ret)

    obj = request.form
    admin = Book(obj)
    db.session.add(admin)
    db.session.commit()
    state = 1
    msg = 'book success'
    ret = {"state": state, "msg": msg}
    return json.dumps(ret)
