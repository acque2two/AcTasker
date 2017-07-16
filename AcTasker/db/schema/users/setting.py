from AcTasker.db.db import db


class Setting(db.EmbeddedDocument):
    # Basic Information
    tags = db.ListField(db.EmbeddedDocumentField("Tag"))
    priorities = db.ListField(db.EmbeddedDocumentField("Priority"))
