from flask import Flask

from config import Config

pugh_app = Flask(__name__)
pugh_app.config.from_object(Config)

from app import routes
