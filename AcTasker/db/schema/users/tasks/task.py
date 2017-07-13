
from AcTasker.db.db import db


class Tasks(db.Document):

    # Basic Information
    name = db.StringField()
    description = db.StringField()
    tags = db.List

    # Tracking
    created_date = db.DateTimeField()
    updated_date = db.DateTimeField()


