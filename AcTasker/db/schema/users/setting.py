from AcTasker.db.db import db


class Setting(db.Document):
    # Basic Information
    tags = db.ListField(db.RelationalField("Tag"))
    priorities = db.ListField(db.RelationalField("Priority"))
