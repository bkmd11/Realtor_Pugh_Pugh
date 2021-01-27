from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config

pugh_app = Flask(__name__)
pugh_app.config.from_object(Config)

db = SQLAlchemy(pugh_app)
migrate = Migrate(pugh_app, db)

from app import routes
