from AcTasker.db.db import db


class Auth(db.Document):
    # Basic Information
    email = db.EmailField()
    name = db.StringField()
    password = db.StringField()
    salt = db.StringField

    updated_date = db.DateTimeField()
