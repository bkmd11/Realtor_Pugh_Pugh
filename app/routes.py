from flask import render_template, url_for, request
from app import pugh_app

@pugh_app.route('/', methods=['GET', 'POST'])
@pugh_app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title='Home Page')