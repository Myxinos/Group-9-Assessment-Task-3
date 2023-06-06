from flask import Blueprint, render_template,redirect,url_for
from .forms import SearchForm
from .models import search_event_by_keyword

bp = Blueprint('main', __name__)


@bp.route('/', methods=['GET'])
def index():
    form = SearchForm()
    return render_template('index.html',form=form)

@bp.route('/search_event', methods=['GET'])
def search_event():
    form = SearchForm()
    if form.validate_on_submit():
        keyword = form.keyword.data
        event = search_event_by_keyword(keyword)
        if event:
            return render_template('event_detail.html', event=event)
    return redirect(url_for('bp.index'))
