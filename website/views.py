from flask import Blueprint, flash, render_template,redirect,url_for
from .forms import SearchForm, ContactForm
from .models import Concert

bp = Blueprint('main', __name__)


@bp.route('/', methods=['GET'])
def index():
    search_form = SearchForm()
    concerts = Concert.query.all()
    contact_form = ContactForm()
    return render_template('index.html', form=search_form, contact_form=contact_form, concerts=concerts)


@bp.route('/event_detail', methods=['GET', 'POST'])
def search_event():
    form = SearchForm()
    if form.validate_on_submit():
        keyword = form.keyword.data
        event = Concert.query.filter_by(eventName=keyword).first()
        if event:
            return render_template('event_detail.html', event=event)
        else:
            flash("No event found with the given keyword.")
    return redirect(url_for('bp.index'))


@bp.route('/category/<category_name>', methods=['GET'])
def category(category_name):
    concerts = Concert.query.filter_by(category=category_name).all()
    return render_template('category.html', concerts=concerts)

@bp.route('/contact', methods=['GET', 'POST'])
def create_contact():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        print("Form has been submitted successfully")
        print(contact_form.user_name.data)
        print(contact_form.email.data)
        return redirect(url_for('bp.index'))
    return render_template('index.html', contact_form=contact_form)
