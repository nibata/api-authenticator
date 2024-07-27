from utils.hump_implementation import to_kebab
from sqlmodel import Field, SQLModel
from typing import Optional
from pydantic import EmailStr
from datetime import date


class UserBase(SQLModel):
    full_name: str = Field(nullable=False, regex="^[a-zA-Z0-9äöüÄÖÜáéíóúÁÉÍÓÚ ]*$")
    email: EmailStr = Field(nullable=False)

    class Config:
        alias_generator = to_kebab
        allow_population_by_field_name = True


class UserCreate(UserBase):
    password: str = Field(nullable=False)
    expiration_date: Optional[date] = None


class UserLogin(SQLModel):
    email: EmailStr = Field(nullable=False)
    password: str = Field(nullable=False)

    class Config:
        alias_generator = to_kebab
        allow_population_by_field_name = True
