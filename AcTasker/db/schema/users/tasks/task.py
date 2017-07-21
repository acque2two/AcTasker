
from AcTasker.db.db import db


class Task(db.EmbeddedDocument):

    # Basic Information
    name = db.StringField()
    description = db.StringField()
    tags = db.EmbeddedDocumentListField("Tag")

    start_date = db.DateTimeField()
    end_date = db.DateTimeField()

    # Tracking
    created_date = db.DateTimeField()
    updated_date = db.DateTimeField()


