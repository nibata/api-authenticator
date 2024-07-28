from controllers.authentication.passwords_controller import PasswordsController
from controllers.authentication.groups_controller import GroupsController
from schemas.authentication.users_schemas import UserLogin, UserCreate
from models.authentication_model import User, UserGroupLink
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select


class UsersController:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_user(self, user_id: int):
        query = select(User).where(User.id == user_id)
        rtn = await self.session.execute(query)
        return rtn.scalars().first()

    async def get_users(self, skip: int = 0, limit: int = 100):
        query = select(User).offset(skip).limit(limit)
        rtn = await self.session.execute(query)
        return rtn.scalars().all()

    async def get_user_by_email(self, email: str):
        query = select(User).where(User.email == email)
        rtn = await self.session.execute(query)
        return rtn.scalars().first()

    async def check_user_password(self, user: UserLogin):
        password = user.password
        db_user = await self.get_user_by_email(user.email)

        if db_user is None:
            return False

        password_controller = PasswordsController(self.session)

        return await password_controller.check_password(db_user.id, password)

    async def get_groups_from_user(self, user_id: int):
        query = select(UserGroupLink).where(UserGroupLink.user_id == user_id)

        groups = await self.session.execute(query)
        groups = groups.all()

        groups_list = [group[0].group_id for group in groups]

        group_controller = GroupsController(self.session)
        rtn = await group_controller.get_groups_by_id_list(groups_list)

        return rtn

    async def create_user(self, user: UserCreate):
        db_user = User(full_name=user.full_name,
                       email=user.email)

        self.session.add(db_user)
        await self.session.flush()

        return db_user

    async def assign_role_to_user(self, user_id: int, group_id: int):
        db_link_group_user = UserGroupLink(user_id=user_id,
                                           group_id=group_id)

        self.session.add(db_link_group_user)

        await self.session.flush()

        return {'UserId': user_id,
                'GroupId': group_id}

    async def set_is_active_user(self, user_id: int, is_active: bool):
        """
        Set the user state. In oder word change de property is_active for the model users
        Parameters
        ----------
        user_id : int
            the id of the user whose state is to be set.
        is_active : bool
            the final value of the state

        Returns
        -------
        model user

        """
        query = select(User).where(User.id == user_id)
        result = await self.session.execute(query)
        user = result.scalar_one()

        user.is_active = is_active

        return user
