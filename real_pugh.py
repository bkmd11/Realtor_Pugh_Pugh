import sys
from app import pugh_app, db

from app.models import User, Listing


@pugh_app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'lr': Listing, 'sys': sys}

# TODO:
#    unittests
#    instructions for ctq selection
#    Handle sql duplication errors
#    error pages
#    add click-able link/check for link in listing field
