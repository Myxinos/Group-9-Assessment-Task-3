import datetime
import time

from flask import render_template, Blueprint

from App.controllers.common.utils import to_json
from App.models.models import Concert, Book, User

index_history = Blueprint('index_history', __name__, )


@index_history.route('history/index.html', methods=['GET', 'POST'])
def index():
    rows = Book.query.filter().order_by(Book.id.desc()).all()
    historys = []
    for row in rows:
        item = to_json(row)
        item['addtime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(item['addtime'])))

        user = User.query.filter(Book.user_id == item['user_id']).first()
        if user is not None:
            item['user'] = user.username

        event = Concert.query.filter(Concert.id == item['concert_id']).first()
        if event is not None:
            item['eventImage'] = event.eventImage
            item['eventName'] = event.eventName
            item['eventDate'] = event.eventDate
            item['startTime'] = event.startTime
            item['endTime'] = event.endTime

        historys.append(item)

    return render_template('history/index.html', **{'historys': historys})
