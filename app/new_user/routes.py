from flask import render_template, url_for, redirect, flash
from flask_login import current_user, login_required

from app import db
from app.new_user import bp
from app.models import User
from app.new_user.forms import NewUser, SetCTQs


@bp.route('/new_user', methods=['GET', 'POST'])
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
        return redirect(url_for('auth.login'))
    return render_template('new_user/new_user.html', form=form)


@bp.route('/set_ctqs', methods=['GET', 'POST'])
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
        current_user.max_total = 9 * len(ctqs)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('set_ctqs.html', form=form)
