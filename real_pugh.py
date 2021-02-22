import sys
from app import pugh_app, db

from app.models import User, Listing


@pugh_app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'lr': Listing, 'sys': sys}

# TODO:
#    unittests
#    welcome/explanation page for new visitors
#    instructions for ctq selection
