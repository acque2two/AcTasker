from AcTasker.db.db import db


class Base(db.Document):
    users = db.ListField(db.ReferenceField("User"))
