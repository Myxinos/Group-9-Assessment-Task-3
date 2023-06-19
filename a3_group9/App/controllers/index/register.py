import json
import time

from flask import render_template, Blueprint, request, flash, url_for, redirect
from App.models.models import User
from App.models.models import db
from App.models.forms import RegisterForm

index_register = Blueprint('index_register', __name__, )


@index_register.route('register/index.html', methods=['GET', 'POST'])
def index():
    form = RegisterForm()
    return render_template("register/index.html", form=form)


@index_register.route('register/check.html', methods=['POST'])
def check():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        telephone = form.telephone.data
        address = form.address.data
        print(f'username:{username}')
        user_info = User.query.filter(User.username == username).first()
        if user_info is None:
            info = User(
                username=username,
                password=password,
                email=email,
                telephone=telephone,
                address=address,
            )
            db.session.add(info)
            db.session.commit()
            flash('register successfully, please login!', 'success')
            return redirect("/index/login/index.html")
        else:
            flash("username already exists",'danger')
            return redirect('/index/register/index.html')

