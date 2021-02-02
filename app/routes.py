import json
from flask import render_template, url_for, request

from app import pugh_app, db
from app.models import User, Listing
from app.forms import AddForm


@pugh_app.route('/', methods=['GET', 'POST'])
@pugh_app.route('/index', methods=['GET', 'POST'])
def index():
    user = User.query.get(1)
    listing = Listing.query.get(1)
    rating = json.loads(listing.rating)
    total = sum(rating)
    rating.append(total)
    listings = [
        {'listing': listing.listing_name, 'rating': rating}
    ]

    col_headers = json.loads(user.ctq)

    return render_template('index.html',
                           title='Home Page',
                           username=user.username,
                           listings=listings,
                           col_headers=col_headers)


@pugh_app.route('/add_listing', methods=['GET', 'POST'])
def add_listing():
    u = User.query.get(1)
    ctq = json.loads(u.ctq)

    form = AddForm()

    if form.validate_on_submit():
        l = form.listing_name.data
        r = [form.ctq_1.data, form.ctq_2.data, form.ctq_3.data]

        nu = Listing(listing_name=l, user_id=u.id, rating=json.dumps(r))

        db.session.add(nu)
        db.session.commit()
    return render_template('add_listing.html', title='New Listing', form=form, ctq=ctq)


