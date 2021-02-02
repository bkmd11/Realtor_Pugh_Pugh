from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from config import Config

pugh_app = Flask(__name__)
pugh_app.config.from_object(Config)

db = SQLAlchemy(pugh_app)
migrate = Migrate(pugh_app, db)
login = LoginManager(pugh_app)
login.login_view = 'login'

from app import routes
