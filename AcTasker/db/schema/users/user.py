from AcTasker.db.db import db


class User(db.EmbeddedDocument):
    # Basic Information
    auth = db.ReferenceField("Auth")

    # Additional Information
    info = db.ReferenceField("Info")
    setting = db.ReferenceField("Setting")
    # Technical Information
    is_disable = db.BooleanField()

    # Tracking
    created_date = db.DateTimeField()

    # Relational
    tasks = db.ListField(db.ReferenceField("Tasks"))
