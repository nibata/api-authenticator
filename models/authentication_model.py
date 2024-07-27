from sqlmodel import Field, Relationship, SQLModel, UniqueConstraint
from schemas.authentication.passwords_schema import PasswordBase
from schemas.authentication.groups_schemas import GroupBase
from schemas.authentication.users_schemas import UserBase
from typing import List


class UserGroupLink(SQLModel, table=True):
    __tablename__ = "user_group_link"
    __table_args__ = (UniqueConstraint("user_id", "group_id", name="unique_user_group_constraint"),
                      {"schema": "authentication"})

    # Fields
    user_id: int = Field(foreign_key="authentication.user.id", primary_key=True)
    group_id: int = Field(foreign_key="authentication.group.id", primary_key=True)


class User(UserBase, table=True):
    """User Class contains standard information for a User."""

    __tablename__ = "user"
    __table_args__ = {"schema": "authentication"}

    # Fields
    id: int = Field(nullable=False, primary_key=True)
    is_active: bool = Field(default=False, nullable=False)

    # Relations
    groups: List["Group"] = Relationship(back_populates="users", link_model=UserGroupLink)


class Group(GroupBase, table=True):
    """Group Class contains standard information for a Groups."""

    __tablename__ = "group"
    __table_args__ = {"schema": "authentication"}

    id: int = Field(nullable=False, primary_key=True)

    # Relations
    users: List["User"] = Relationship(back_populates="groups", link_model=UserGroupLink)


class Password(PasswordBase, table=True):
    """Password Class contains standard information for a Passwords for users."""

    __tablename__ = "password"
    __table_args__ = {"schema": "authentication"}

    id: int = Field(primary_key=True, nullable=False)
    user_id: int = Field(foreign_key="authentication.user.id")
    hashed_password: str = Field(nullable=False, max_length=120)

