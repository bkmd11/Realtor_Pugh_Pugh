from flask import render_template
from app import pugh_app


@pugh_app.route('/')
@pugh_app.route('/home')
def home():
    return render_template('home.html', title='Welcome')
