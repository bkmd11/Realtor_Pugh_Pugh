from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

from config import Config

pugh_app = Flask(__name__)
pugh_app.config.from_object(Config)

db = SQLAlchemy(pugh_app)
migrate = Migrate(pugh_app, db)
login = LoginManager(pugh_app)
login.login_view = 'auth.login'
bootstrap = Bootstrap(pugh_app)

from app.auth import bp as auth_bp
pugh_app.register_blueprint(auth_bp, url_prefix='/auth')

from app.new_user import bp as new_user_bp
pugh_app.register_blueprint(new_user_bp, url_prefix='/new_user')

from app.errors import bp as error_bp
pugh_app.register_blueprint(error_bp)

from app.main import bp as main_bp
pugh_app.register_blueprint(main_bp, url_prefix='/main')

from app import routes, models
