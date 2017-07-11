from flask_sqlalchemy import SQLAlchemy

from config import CONFIG


class Database:
    def __init__(self, app):
        app.config.from_object('config.CONFIG.DB.' + 'DEVELOPMENT' if CONFIG.DEV else "PRODUCTION")

        self.conn = SQLAlchemy(app, session_options={'autoflush': False})

    def session(self):
        return self.conn.session


from main import app

db = Database(app)
