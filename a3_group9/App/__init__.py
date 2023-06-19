from flask import Flask, redirect, render_template
from config.urls import register_blueprints
from App.middleware.checkuser import index_middleware
from App.models.models import db, User

from flask_login import logout_user, current_user, UserMixin, LoginManager, login_manager, login_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, static_folder='static', static_url_path='/static')


def register_plugin(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()


def create_app():

    app.config.from_object('config.dbs')
    app.secret_key = '111111'
    login_manager = LoginManager()
    login_manager.session_protection = 'strongpwd123'
    login_manager.login_view = 'index_login.index'
    login_manager.init_app(app)

    @app.login_manager.user_loader
    def user_loader(user_id):
        return User.query.get(user_id)

    register_blueprints(app)
    register_plugin(app)
    index_middleware(app)

    return app


# app = create_app()
# index_middleware(app)


@app.route('/')
def home():
    return redirect("/index/index/index.html")
#    return render_template("base.html")

