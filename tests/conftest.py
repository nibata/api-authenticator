from sqlalchemy.orm import sessionmaker
from sqlmodel import create_engine
from alembic.config import Config
from alembic import command
import pytest
import os


# Database setup
@pytest.fixture(scope="session")
def db():
    # Create a test database engine
    DB_DRIVER = os.environ.get("DB_DRIVER")
    DB_HOST = os.environ.get("DB_HOST")
    DB_PORT = os.environ.get("DB_PORT")
    DB_USER = os.environ.get("DB_USER")
    DB_PASS = os.environ.get("DB_PASS")
    DB_TEST = os.environ.get("DB_TEST")
    DB_ASYNC_DRIVER = os.environ.get("DB_ASYNC_DRIVER")
    URI_DB = f"{DB_DRIVER}+{DB_ASYNC_DRIVER}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_TEST}"

    engine = create_engine(URI_DB)
    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Run Alembic migrations
    alembic_cfg = Config("alembic.ini")
    # I couldn't make it work with an async url, doesn't matter due I don't really need it
    # in the upgrade of the database
    command.upgrade(alembic_cfg, "head")

    # Create a new session for the tests
    session = Session()

    yield session

    # Teardown: Drop the test database
    session.close()
    engine.dispose()
    command.downgrade(alembic_cfg, "base")
