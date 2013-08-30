try:
    from permissions import db
except ImportError:
    raise Exception("Permissions app must be initialized before importing \
                    models")

class Role(db.Model):
    def __init__(self):
        pass

class PermsUser(db.Model):
    role = Role()
    def __init__(self):
        pass


