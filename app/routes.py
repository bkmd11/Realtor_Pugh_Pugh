from flask import render_template, url_for, request, redirect, flash
from flask_login import current_user, login_user, logout_user, login_required

from werkzeug.urls import url_parse

from app import pugh_app, db
from app.models import User, Listing
from app.forms import AddForm, LoginForm


@pugh_app.route('/', methods=['GET', 'POST'])
@pugh_app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    listings = current_user.user_listings()
    col_headers = current_user.ctq

    return render_template('index.html',
                           title='Home Page',
                           username=current_user.username,
                           listings=listings,
                           col_headers=col_headers)


@pugh_app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@pugh_app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@pugh_app.route('/add_listing', methods=['GET', 'POST'])
@login_required
def add_listing():
    user = User.query.get(1)
    ctq = current_user.ctq

    form = AddForm()

    if form.validate_on_submit():
        listing = form.listing_name.data
        rating = [form.ctq_1.data, form.ctq_2.data, form.ctq_3.data]

        total = sum(rating)
        rating.append(total)

        nu = Listing(listing_name=listing, user_id=user.id, rating=rating)

        db.session.add(nu)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add_listing.html', title='New Listing', form=form, ctq=ctq)


