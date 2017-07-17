
from AcTasker.db.db import db


class Task(db.Document):

    # Basic Information
    name = db.StringField()
    description = db.StringField()
    tags = db.ListField(db.ReferenceField("Tag"))

    start_date = db.DateTimeField()
    end_date = db.DateTimeField()

    # Tracking
    created_date = db.DateTimeField()
    updated_date = db.DateTimeField()


