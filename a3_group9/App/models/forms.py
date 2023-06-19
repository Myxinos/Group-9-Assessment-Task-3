from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, FileField, TimeField, SubmitField, TextAreaField, IntegerField, HiddenField, SelectField
from wtforms.validators import InputRequired, Length, Email

from .models import *


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(
        1, 20)], render_kw={'class': 'form-control'})
    password = PasswordField('Password', validators=[InputRequired(), Length(
        1, 128)], render_kw={'class': 'form-control'})
    submit = SubmitField('Login', render_kw={
                         'class': 'btn btn-primary w-25 login'})


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(
        1, 20)], render_kw={'class': 'form-control'})
    email = StringField('Email', validators=[InputRequired(), Length(
        1, 200), Email()], render_kw={'class': 'form-control'})
    telephone = StringField('Telephone', validators=[InputRequired(), Length(
        1, 200)], render_kw={'class': 'form-control'})
    address = TextAreaField('Address', validators=[InputRequired(), Length(
        1, 200)], render_kw={'class': 'form-control'})
    password = PasswordField('Password', validators=[InputRequired(), Length(
        1, 128)], render_kw={'class': 'form-control'})
    repassword = PasswordField('RePassword', validators=[
                               InputRequired(), Length(1, 128)], render_kw={'class': 'form-control'})
    submit = SubmitField('Register', render_kw={
                         'class': 'btn btn-primary w-25 login'})


class CommentForm(FlaskForm):
    concert_id = HiddenField('concert_id', validators=[
                             InputRequired(), Length(1, 20)])
    content = TextAreaField('content', validators=[InputRequired(), Length(
        1, 128)], render_kw={'class': 'form-control mb-3'})
    submit = SubmitField('Post a Comment', render_kw={
                         'class': 'btn btn-primary w-25 login'})


class EventForm(FlaskForm):
    price = IntegerField('price', validators=[InputRequired()], render_kw={
                         'class': 'form-control'})
    file = FileField('file', validators=[InputRequired()], render_kw={
                     'class': 'form-control'})
    eventName = StringField('eventName', validators=[Length(
        1, 255)], render_kw={'class': 'form-control'})
    eventOrganizer = StringField('eventOrganizer', validators=[
                                 Length(1, 255)], render_kw={'class': 'form-control'})
    category = StringField('category', validators=[Length(
        1, 255)], render_kw={'class': 'form-control'})
    musician = StringField('musician', validators=[Length(
        1, 255)], render_kw={'class': 'form-control'})
    tags = StringField('tags', validators=[Length(1, 255)], render_kw={
                       'class': 'form-control'})
    eventDate = DateField('eventDate', validators=[
                          InputRequired()], render_kw={'class': 'form-control'})
    content = TextAreaField('content', validators=[InputRequired()], render_kw={
                            'class': 'form-control'})
    startTime = TimeField('startTime', validators=[
                          InputRequired()], render_kw={'class': 'form-control'})
    endTime = TimeField('endTime', validators=[InputRequired()], render_kw={
                        'class': 'form-control'})
    timeZone = StringField('timeZone', validators=[Length(
        1, 255)], render_kw={'class': 'form-control'})
    language = StringField('language', validators=[Length(
        1, 255)], render_kw={'class': 'form-control'})
    locationType = SelectField('locationType',
                               validators=[InputRequired()],
                               render_kw={'class': 'form-control'},
                               choices=[(0, 'Select Location'), (1, 'Venue'),
                                        (2, 'Online Event'), (3, 'To be announced')],
                               default=0,
                               coerce=int)
    location = StringField('location', validators=[Length(
        1, 255)], render_kw={'class': 'form-control'})
    submit = SubmitField('Add a Event', render_kw={
                         'class': 'btn btn-primary w-25 login'})


# this is the search form
class SearchForm(FlaskForm):
    keyword = StringField('Search Event Name', validators=[InputRequired()])
    # submit button
    submit = SubmitField('Search')
