from utils.hump_implementation import to_kebab
from configs.settings import SECRET_KEY
from sqlmodel import SQLModel, Field
from datetime import datetime, date
from pydantic import EmailStr
from typing import Optional
import hashlib


class PasswordBase(SQLModel):
    creation_date: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    is_active: bool = Field(nullable=False, default=True)
    expiration_date: Optional[date] = Field(nullable=True)

    class Config:
        alias_generator = to_kebab
        allow_population_by_field_name = True

    @staticmethod
    def set_password(pwd: str) -> str:
        """Genera password hasheada mediante método md5

        Parameters
        ----------
        pwd : str
            Password a hashear

        Returns
        -------
        str
            Password hasheada
        """

        salt = SECRET_KEY
        password_to_hash = pwd + salt
        password = hashlib.sha256(password_to_hash.encode()).hexdigest()

        return password


class PasswordRead(SQLModel):
    user_id: int
    is_active: bool
    expiration_date: Optional[date] = None

    class Config:
        alias_generator = to_kebab
        allow_population_by_field_name = True


class PasswordUpdate(SQLModel):
    email: EmailStr = Field(nullable=False)
    current_password: str = Field(nullable=False)
    new_password: str = Field(nullable=False)
    expiration_date: Optional[date] = None

    class Config:
        alias_generator = to_kebab
        allow_population_by_field_name = True


class PasswordDeactivate(SQLModel):
    email: EmailStr = Field(nullable=False)

    class Config:
        alias_generator = to_kebab
        allow_population_by_field_name = True


class PasswordCreate(SQLModel):
    email: EmailStr = Field(nullable=False)
    password: str = Field(nullable=False)
    expiration_date: Optional[date] = None

    class Config:
        alias_generator = to_kebab
        allow_population_by_field_name = True