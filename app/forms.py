from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, AnyOf


class AddForm(FlaskForm):
    listing_name = StringField('Listing Name', validators=[DataRequired()])
    ctq_1 = IntegerField('Grade', validators=[DataRequired(), AnyOf([1, 5, 9])])
    ctq_2 = IntegerField('Grade', validators=[DataRequired(), AnyOf([1, 5, 9])])
    ctq_3 = IntegerField('Grade', validators=[DataRequired(), AnyOf([1, 5, 9])])

    submit = SubmitField('Update')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
