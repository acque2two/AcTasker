from AcTasker.db.db import db


class Setting(db.EmbeddedDocument):
    # Basic Information
    tags = db.EmbeddedDocumentListField("Tag")
    priorities = db.EmbeddedDocumentListField("Priority")
