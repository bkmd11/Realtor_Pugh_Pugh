from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, AnyOf, Optional, Email, EqualTo


class AddForm(FlaskForm):
    listing_name = StringField('Listing Name', validators=[DataRequired()])
    ctq_1 = IntegerField('Grade', validators=[AnyOf([1, 5, 9]), Optional()])
    ctq_2 = IntegerField('Grade', validators=[AnyOf([1, 5, 9]), Optional()])
    ctq_3 = IntegerField('Grade', validators=[AnyOf([1, 5, 9]), Optional()])
    ctq_4 = IntegerField('Grade', validators=[AnyOf([1, 5, 9]), Optional()])
    ctq_5 = IntegerField('Grade', validators=[AnyOf([1, 5, 9]), Optional()])
    ctq_6 = IntegerField('Grade', validators=[AnyOf([1, 5, 9]), Optional()])
    ctq_7 = IntegerField('Grade', validators=[AnyOf([1, 5, 9]), Optional()])

    submit = SubmitField('Update')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class NewUser(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
