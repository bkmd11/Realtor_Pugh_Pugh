from flask import render_template, url_for, request, redirect, flash
from flask_login import current_user, login_user, logout_user

from werkzeug.urls import url_parse

from app.auth import bp
from app.models import User
from app.auth.forms import LoginForm


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user_email = User.query.filter_by(email=form.email.data).first()
        if user_email is None or not user_email.check_password(form.password.data):
            flash('Invalid credentials')
            return redirect(url_for('auth.login'))
        login_user(user_email, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)
    return render_template('auth/login.html', title='Sign In', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
