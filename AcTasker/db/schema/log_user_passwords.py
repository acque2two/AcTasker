from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, String, text, Index
from sqlalchemy.orm import relationship

from AcTasker.db.db import db
from AcTasker.db.schema.users import Users


class UserPasswordChangelog(db.Model):
    __tablename__ = 'user_password_changelogs'
    __table_args__ = (
        Index('login_email', 'email', 'password'),
        Index('login_uid', 'id', 'password'),
    )

    # ForeignKey to Users.id
    user_id = Column(ForeignKey(Users.id), nullable=False)

    # Logging New Password.
    new_password = Column(String(128), nullable=False)

    # Tracking
    created_date = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))

