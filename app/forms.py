from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class AddForm(FlaskForm):
    listing_name = StringField('Listing Name', validators=[DataRequired()])

    def get_data(self, name):
        data = getattr(self, name)
        return data.data


