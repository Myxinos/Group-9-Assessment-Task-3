

from flask import request, session, redirect

from App.models.models import User
from App.models.models import db


def index_middleware(app):

    @app.after_request
    def after_request(environ):
        db.session.close()
        return environ
