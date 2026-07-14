import enum
from app.config.database import Base
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, text, Enum


class UserStatus(str, enum.Enum):
    NOT_ARRIVED = "not_arrived"
    IN_PARTY = "in_party"
    DEPARTED = "departed"


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    nick_name = Column(String, nullable=False)
    contact_info = Column(String, nullable=False)
    address = Column(String, nullable=False)
    status = Column(Enum(UserStatus), nullable=False, default=UserStatus.NOT_ARRIVED)
    is_admin = Column(Boolean, nullable=False, default=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))
