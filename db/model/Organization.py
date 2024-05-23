from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, DateTime
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime
import bcrypt
from db.base import Base


class Organization(Base):
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, unique=True)
    uuid = Column(String(255), unique=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(255), nullable=False)
    mail_id = Column(String(256), nullable=False, unique=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)

    # Relationship
    user = relationship("User", back_populates="organization")

    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()). decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))


class User(Base):
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, unique=True)
    uuid = Column(String(255), unique=True, default=lambda: str(uuid.uuid4()))
    organization_id = Column(Integer, ForeignKey('organization.id'))
    name = Column(String(255), nullable=False)
    mail_id = Column(String(256), nullable=False, unique=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)

    # Relationship
    organization = relationship("Organization", back_populates="user")
    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()). decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))