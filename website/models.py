from flask_login import UserMixin
from . import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)

def search_event_by_keyword(keyword):
    return db.session.query(Event).filter(Event.name.contains(keyword)).first()
