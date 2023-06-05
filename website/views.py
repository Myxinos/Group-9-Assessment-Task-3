from flask import Blueprint, render_template,redirect,url_for
from .forms import SearchForm

bp = Blueprint('main', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        event_name = form.event_name.data
        result = search_by_event_name(event_name)
        if result:
            return redirect(url_for('main.event_detail', event_name=event_name))
    return render_template('index.html', form=form)
