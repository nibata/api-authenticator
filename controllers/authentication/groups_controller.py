from schemas.authentication.groups_schemas import GroupCreate
from sqlmodel.ext.asyncio.session import AsyncSession
from models.authentication_model import Group
from sqlalchemy import select
from typing import List


class GroupsController:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_groups_by_id_list(self, group_ids_list: List):
        query = select(Group).where(Group.id.in_(group_ids_list))
        rtn = await self.session.execute(query)
        return rtn.scalars().all()

    async def get_group_by_id(self, group_id: int):
        query = select(Group).where(Group.id == group_id)
        rtn = await self.session.execute(query)
        return rtn.scalars().first()

    async def get_group_by_code(self, code: str):
        query = select(Group).where(Group.code == code)
        rtn = await self.session.execute(query)
        return rtn.scalars().first()

    async def get_groups(self):
        query = select(Group)
        rtn = await self.session.execute(query)
        return rtn.scalars().all()

    async def create_group(self, group: GroupCreate):
        db_group = Group(code=group.code,
                         description=group.description)

        self.session.add(db_group)
        await self.session.flush()

        return db_group
