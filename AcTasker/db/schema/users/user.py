from AcTasker.db.db import db


class User(db.Document):
    # Basic Information
    auth = db.EmbeddedDocumentField("Auth")

    # Additional Information
    info = db.EmbeddedDocumentField("Info")
    setting = db.EmbeddedDocumentField("Setting")
    # Technical Information
    is_disable = db.BooleanField()

    # Tracking
    created_date = db.DateTimeField()

    # Relational
    tasks = db.EmbeddedDocumentListField("Task")
