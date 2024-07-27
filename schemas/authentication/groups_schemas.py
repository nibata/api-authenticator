from sqlmodel import Field, SQLModel
from utils.hump_implementation import to_kebab


class GroupBase(SQLModel):
    code: str = Field(nullable=False, unique=True, regex="^[a-zA-Z0-9äöüÄÖÜáéíóúÁÉÍÓÚ ]*$")
    description: str = Field(nullable=True)

    class Config:
        alias_generator = to_kebab
        allow_population_by_field_name = True


class GroupRead(GroupBase):
    id: int


class GroupCreate(GroupBase):
    pass
