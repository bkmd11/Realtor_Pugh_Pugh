from flask import render_template, url_for, redirect
from flask_login import current_user, login_required
from wtforms import IntegerField, SubmitField
from wtforms.validators import AnyOf

from app import pugh_app, db
from app.models import Listing
from app.forms import AddForm


@pugh_app.route('/', methods=['GET', 'POST'])
@pugh_app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    listings = current_user.user_listings().order_by(Listing.total.desc())
    col_headers = current_user.ctq
    good_range = current_user.max_total*.8
    bad_range = current_user.max_total*.5

    if col_headers is None:
        return redirect(url_for('set_ctqs'))
    return render_template('index.html',
                           title='Home Page',
                           username=current_user.username,
                           listings=listings,
                           col_headers=col_headers,
                           max_total=current_user.max_total,
                           good_range=good_range,
                           bad_range=bad_range)


@pugh_app.route('/add_listing', methods=['GET', 'POST'])
@login_required
def add_listing():
    user = current_user.id
    ctq = current_user.ctq

    class F(AddForm):
        pass

    for i in ctq:
        setattr(F, i, IntegerField(label=i, validators=[AnyOf([1, 5, 9])]))
    setattr(F, 'submit', SubmitField('Update'))

    form = F()

    if form.validate_on_submit():
        listing = form.listing_name.data

        ratings = [form.get_data(i) for i in form.data if i in ctq]

        total = sum(ratings)

        nu = Listing(listing_name=listing, user_id=user, rating=ratings, total=total)

        db.session.add(nu)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add_listing.html', title='New Listing', form=form, ctq=ctq)
