from flask import Blueprint, flash, render_template, request, url_for, redirect
from werkzeug.security import generate_password_hash,check_password_hash
#from .models import User
from .forms import LoginForm,RegisterForm
from flask_login import login_user, login_required,logout_user
from . import db

#create a blueprint
bp = Blueprint('auth', __name__)

# this is a hint for a login function
# @bp.route('/login', methods=['GET', 'POST'])
# def authenticate(): #view function
#     print('In Login View function')
#     login_form = LoginForm()
#     error=None
#     if(login_form.validate_on_submit()==True):
#         user_name = login_form.user_name.data
#         password = login_form.password.data
#         user = User.query.filter_by(name=user_name).first()
#         if user is None:
#             error='Incorrect credentials supplied'
#         elif not check_password_hash(user.password_hash, password): # takes the hash and password
#             error='Incorrect credentials supplied'
#         if error is None:
#             login_user(user)
#             nextp = request.args.get('next') #this gives the url from where the login page was accessed
#             print(nextp)
#             if next is None or not nextp.startswith('/'):
#                 return redirect(url_for('index'))
#             return redirect(nextp)
#         else:
#             flash(error)
#     return render_template('user.html', form=login_form, heading='Login')
