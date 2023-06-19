import datetime

from flask import redirect, render_template, Blueprint, url_for
from sqlalchemy import func
from App.models.forms import SearchForm

from App.controllers.common.utils import to_json
from App.models.models import Concert

index_index = Blueprint('index_index', __name__, )


@index_index.route('index/index.html', methods=['GET', 'POST'])
def index():
    search_form = SearchForm()
    today = datetime.datetime.now().strftime('%Y-%m-%d')

    events = Concert.query.filter(func.strftime('%Y-%m-%d', Concert.eventDate) == today).order_by(Concert.id.desc()).all()
    Upcoming = Concert.query.filter(func.strftime('%Y-%m-%d', Concert.eventDate) > today).order_by(Concert.id.desc()).all()

    rows = Concert.query.filter().order_by(Concert.id.desc()).all()
    categorys = []

    datas = []

    for row in rows:
        item = to_json(row)

        if item['category'] not in categorys:
            categorys.append(item['category'])
            datas.append(item)

    return render_template('index/index.html', search_form=search_form, events= events, Upcoming= Upcoming, datas=datas)

@index_index.route('/event_detail', methods=['GET', 'POST'])
def search_event():
    search_form = SearchForm()
    if search_form.validate_on_submit():
        keyword = search_form.keyword.data
        concert_detail = Concert.query.filter(Concert.eventName.like('%'+keyword+'%')).first()
        if concert_detail:
            return redirect(url_for('index_event.detail', id=concert_detail.id))

    return redirect(url_for('index_index.index'))
