from AcTasker.db.db import db


class User(db.Document):
    # Basic Information
    auth = db.EmbeddedDocumentField("Auth")

    # Additional Information
    info = db.EmbeddedDocumentField("Info")
    setting = db.ReferenceField("Setting", reverse_delete_rule=db.CASCADE)
    # Technical Information
    is_disable = db.BooleanField()

    # Tracking
    created_date = db.DateTimeField()

    # Relational
    tasks = db.ListField(db.ReferenceField("Tasks"))
