from AcTasker.db.db import db


class Priority(db.EmbeddedDocument):
    # Basic Information
    name = db.StringField()
    description = db.StringField()

    priority_level = db.IntField()

    # Tracking
    created_date = db.DateTimeField()
    updated_date = db.DateTimeField()
