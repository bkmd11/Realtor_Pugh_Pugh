from app import pugh_app, db

from app.models import User, Listing, CTQ

@pugh_app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'lr': Listing, 'ctq': CTQ}
