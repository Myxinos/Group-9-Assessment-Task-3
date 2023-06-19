from flask import render_template, Blueprint, request

from App.models.models import Concert
from flask_login import login_required

index_category = Blueprint('index_category', __name__, )

@index_category.route('category/index.html', methods=['GET', 'POST'])
@login_required
def index():
    category = request.args.get("category")

    events = Concert.query.filter(Concert.category == category).order_by(Concert.id.desc()).all()

    print(events)

    return render_template('category/index.html', **{'events': events, 'category': category})
