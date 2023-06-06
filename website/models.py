from . import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    address= db.Column(db.String(256), nullable=False)
    status = db.Column(db.String(64), nullable=False)
    category= db.Column(db.String(64), index=True, nullable=False)
    image = db.Column(db.String(60), nullable=False, default='default.jpg')

def search_event_by_keyword(keyword):
    return db.session.query(Event).filter(Event.name.contains(keyword)).first()
