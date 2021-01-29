from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired


class AddForm(FlaskForm):
    listing_name = StringField('Listing Name')
    ctq_1 = IntegerField('Grade')
    ctq_2 = IntegerField('Grade')
    ctq_3 = IntegerField('Grade')