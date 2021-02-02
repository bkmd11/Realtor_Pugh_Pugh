from flask import render_template, url_for, request, redirect, flash
from flask_login import current_user, login_user, logout_user, login_required
from wtforms import IntegerField, SubmitField
from wtforms.validators import AnyOf

from werkzeug.urls import url_parse

from app import pugh_app, db
from app.models import User, Listing
from app.forms import AddForm, LoginForm, NewUser, SetCTQs


@pugh_app.route('/', methods=['GET', 'POST'])
@pugh_app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    listings = current_user.user_listings()
    col_headers = current_user.ctq

    if col_headers is None:
        return redirect(url_for('set_ctqs'))

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
    user = current_user.id
    ctq = current_user.ctq

    class F(AddForm):
        pass

    for i in ctq:
        setattr(F, i, IntegerField(label=i, validators=[AnyOf([1, 5, 9])]))
    setattr(F, 'submit', SubmitField('Update')
)
    form = F()

    if form.validate_on_submit():
        listing = form.listing_name.data

        ratings = [form.get_data(i) for i in form.data if i in ctq]

        total = sum(ratings)
        ratings.append(total)

        nu = Listing(listing_name=listing, user_id=user, rating=ratings)

        db.session.add(nu)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add_listing.html', title='New Listing', form=form, ctq=ctq)


@pugh_app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = NewUser()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are now registered!')
        return redirect(url_for('login'))
    return render_template('new_user.html', form=form)


@pugh_app.route('/set_ctqs', methods=['GET', 'POST'])
@login_required
def set_ctqs():
    form = SetCTQs()

    if form.validate_on_submit():
        ctq = [
            form.ctq_1.data,
            form.ctq_2.data,
            form.ctq_3.data,
            form.ctq_4.data,
            form.ctq_5.data,
            form.ctq_6.data,
            form.ctq_7.data
        ]
        ctqs = [i for i in ctq if i]

        current_user.ctq = ctqs
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('set_ctqs.html', form=form)
