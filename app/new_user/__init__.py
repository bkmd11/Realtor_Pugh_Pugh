from flask import Blueprint

bp = Blueprint('new_user', __name__)

from app.new_user import routes
