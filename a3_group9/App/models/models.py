from datetime import datetime

from flask import session
from sqlalchemy import Column, Integer, String, Float, Text
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from flask_login import UserMixin, current_user


class SQLAlchemy(_SQLAlchemy):
    def auto_commit(self):
        try:
            yield
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e


db = SQLAlchemy(query_class=BaseQuery)


class Models(db.Model):
    db = db
    __abstract__ = True

    addtime = Column('addtime', Integer)
    updatetime = Column('updatetime', Integer)

    def __init__(self):
        self.addtime = int(datetime.now().timestamp())
        self.updatetime = int(datetime.now().timestamp())

    def __getitem__(self, item):
        return getattr(self, item)

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)


class User(UserMixin, Models):
    """user table"""
    __tablename__ = 's_user'
    id = Column(Integer, unique=True, nullable=True, primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=True, unique=True, default='')
    password = Column(String(32))
    email = Column(String(100), nullable=True, unique=True, default='')
    telephone = Column(String(20))
    address = Column(String(255))
    addtime = Column(Integer, default=0)
    updatetime = Column(Integer, default=0)

    def __init__(self, username, password, email, telephone, address):
        super(User, self).__init__()
        self.username = username
        self.password = password
        self.email = email
        self.telephone = telephone
        self.address = address

    def is_authenticated(self):
        
        return True

    def is_active(self):
        
        return True

    def is_anonymous(self):
        
        return False

    def get_id(self):
        
        return self.id

class Concert(Models):
    """event table"""
    __tablename__ = 's_concert'
    id = Column(Integer, unique=True, nullable=True, primary_key=True, autoincrement=True)
    user_id = Column(Integer, default=0)
    price = Column(Integer, default=0)
    eventImage = Column(String(255), nullable=True, default='')
    eventName = Column(String(255), nullable=True, default='')
    eventOrganizer = Column(String(255), nullable=True, default='')
    category = Column(String(255), nullable=True, default='')
    musician = Column(String(255), nullable=True, default='')
    tags = Column(String(255), nullable=True, default='')
    eventDate = Column(String(50), default='')
    content = Column(Text, nullable=True, default='')
    startTime = Column(String(50), default='')
    endTime = Column(String(50), default='')
    timeZone = Column(String(50), default='')
    language = Column(String(50), default='')
    locationType = Column(Integer, default=0)
    location = Column(String(255), default='')
    addtime = Column(Integer, default=0)
    updatetime = Column(Integer, default=0)

    def __init__(self, obj):
        super(Concert, self).__init__()

        # user_info = session.get('user_info')
        self.user_id = current_user.id
        self.price = obj.get('price')
        self.eventImage = obj.get('eventImage')
        self.eventName = obj.get('eventName')
        self.eventOrganizer = obj.get('eventOrganizer')
        self.category = obj.get('category')
        self.musician = obj.get('musician')
        self.tags = obj.get('tags')
        self.eventDate = obj.get('eventDate')
        self.content = obj.get('content')
        self.startTime = obj.get('startTime')
        self.endTime = obj.get('endTime')
        self.timeZone = obj.get('timeZone')
        self.language = obj.get('language')
        self.locationType = obj.get('locationType')
        self.location = obj.get('location')


class Comment(Models):
    """comment table"""
    __tablename__ = 's_comment'
    id = Column(Integer, unique=True, nullable=True, primary_key=True, autoincrement=True)
    user_id = Column(Integer, default=0)
    concert_id = Column(Integer, default=0)
    content = Column(Text, nullable=True, default='')
    addtime = Column(Integer, default=0)
    updatetime = Column(Integer, default=0)

    def __init__(self, obj):
        super(Comment, self).__init__()
        self.concert_id = obj.get('concert_id')
        self.content = obj.get('content')
        self.user_id = current_user.id


class Book(Models):
    """booking table"""
    __tablename__ = 's_book'
    id = Column(Integer, unique=True, nullable=True, primary_key=True, autoincrement=True)
    user_id = Column(Integer, default=0)
    concert_id = Column(Integer, default=0)
    number = Column(Integer, default=0)
    price = Column(Float, default=0.0)
    totalPrice = Column(Float, default=0.0)
    addtime = Column(Integer, default=0)
    updatetime = Column(Integer, default=0)

    def __init__(self, obj):
        super(Book, self).__init__()

        self.concert_id = obj.get('concert_id')
        self.number = obj.get('number')
        self.price = obj.get('price')
        self.totalPrice = obj.get('totalPrice')

        user_info = session.get('user_info')
        self.user_id = user_info['id']
