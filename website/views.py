from flask import Blueprint

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return '<h1>Starter code for the assessment<h1>'