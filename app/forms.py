from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, AnyOf, Optional, Email, EqualTo


class AddForm(FlaskForm):
    listing_name = StringField('Listing Name', validators=[DataRequired()])


    def get_data(self, name):
        data = getattr(self, name)
        return data.data


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


class SetCTQs(FlaskForm):
    ctq_1 = StringField('Criteria:', validators=[Optional()])
    ctq_2 = StringField('Criteria:', validators=[Optional()])
    ctq_3 = StringField('Criteria:', validators=[Optional()])
    ctq_4 = StringField('Criteria:', validators=[Optional()])
    ctq_5 = StringField('Criteria:', validators=[Optional()])
    ctq_6 = StringField('Criteria:', validators=[Optional()])
    ctq_7 = StringField('Criteria:', validators=[Optional()])

    submit = SubmitField('Done')
