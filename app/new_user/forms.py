from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Optional, Email, EqualTo


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
