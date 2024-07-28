from configs.settings import DB_ASYNC_DRIVER, DB_DRIVER, DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME, UNITTEST, DB_TEST
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

if UNITTEST == "True":
    DB_URI = f"{DB_DRIVER}+{DB_ASYNC_DRIVER}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_TEST}"
else:
    DB_URI = f"{DB_DRIVER}+{DB_ASYNC_DRIVER}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

ENGINE = create_async_engine(DB_URI, future=True, poolclass=NullPool)


async def get_session() -> AsyncSession:
    async_session = sessionmaker(ENGINE, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session
