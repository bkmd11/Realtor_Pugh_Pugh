import json
from flask import render_template, url_for, request

from app import pugh_app, db
from app.models import User, Listing


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


