from AcTasker.db.db import db


class Info(db.Document):
    # Additional Information
    first_name = db.StringField()
    last_name = db.StringField()
    display_name = db.StringField()

    # Technical Information
    is_disable = db.BooleanField()

    # Tracking
    updated_date = db.DateTimeField()
