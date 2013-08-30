from flask_permissions import FlaskPermissions

from sqla import SQLAlchemy

db = SQLAlchemy()
permissions = FlaskPermissions()
permissions.init_app(None, db)

from flask_permissions.models import *

class User(PermsUser):
    id = db.Column()

    def __init__(self):
        print self.id, self.role
