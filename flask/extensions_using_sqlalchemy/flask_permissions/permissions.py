
class FlaskPermissions:
    def __init__(self):
        pass
    
    def init_app(self, app, local_db):
        self.app = app
        global db
        db = local_db

