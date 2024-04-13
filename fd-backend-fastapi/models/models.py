from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Uuid, Date, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column, validates
from uuid import UUID, uuid4
from datetime import date
import re

from ..db.db import Base


class Users(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    email: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String, unique=True)
    sign_up_date: Mapped[date] = mapped_column(Date)

    @validates('email')
    def validate_email(self, key, value):
        pattern = r'^[\w\-\.]+@([\w-]+\.)+[\w-]{2,}$'
        if re.match(pattern):
            return value
        else:
            raise ValueError("Invalid email format.")


class Auth(Base):
    __tablename__ = "auth"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    auth_token: Mapped[str] = mapped_column(String(50), unique=True)
    login_datetime: Mapped[date] = mapped_column(Date)
    active: Mapped[bool] = mapped_column(Boolean, default=False)


class Uploads(Base):
    __tablename__ = "uploads"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    filename: Mapped[str] = mapped_column(String(50))
    upload_datetime: Mapped[date] = mapped_column(Date)
