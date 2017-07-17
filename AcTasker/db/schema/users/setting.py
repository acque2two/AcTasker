from AcTasker.db.db import db


class Setting(db.Document):
    # Basic Information
    tags = db.ListField(db.ReferenceField("Tag"))
    priorities = db.ListField(db.ReferenceField("Priority"))
