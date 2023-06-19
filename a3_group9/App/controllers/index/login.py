import json

from flask import render_template, Blueprint, request, session, redirect, flash, url_for
from App.models.models import User
from App.models.forms import LoginForm
from flask_login import login_user, login_required, logout_user, current_user


index_login = Blueprint('index_login', __name__, )


@index_login.route('login/index.html', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    return render_template("login/index.html", form=form)


@index_login.route('login/check', methods=['POST'])
def check():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user_info = User.query.filter(User.username == username).first()
        if user_info is None:
            flash("username does not exist", "danger")
            return redirect(url_for("index_login.index"))
        else:
            if user_info.password != password:
                flash("wrong password", "danger")
                return redirect(url_for("index_login.index"))
            else:
                login_info = {"id": user_info.id, "username": username}
                login_user(user_info)
                print(current_user.username)
                flash("login success", "success")
                return redirect(url_for("index_index.index"))


@index_login.route('login/logout.html', methods=['GET', 'POST'])
def logout():
    logout_user()
    flash('You have been logout!', 'success')
    return redirect("/index/login/index.html")
