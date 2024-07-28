import os


APP_NAME = "API Authenticator"
APP_AUTHOR = "NICOLAS BACQUET"
APP_EMAIL = "nicolas@bacquet.cl"
APP_VERSION = "0.0.0"
APP_DESCRIPTION = "APP TO MANAGE AUTHENTICATIONS WITH API"
DB_DRIVER = os.environ.get("DB_DRIVER")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_NAME = os.environ.get("DB_NAME")
UNITTEST = os.environ.get("UNITTEST")
DB_TEST = os.environ.get("DB_TEST")
SECRET_KEY = os.environ.get("SECRET_KEY")
SENTRY_DNS = os.environ.get("SENTRY_DNS")
JWT_SECRET = os.environ.get("JWT_SECRET")
JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM")
DB_ASYNC_DRIVER = os.environ.get("DB_ASYNC_DRIVER")
CRYPTO_KEY = os.environ.get("CRYPTO_KEY")
APP_ADMIN_EMAIL = os.environ.get("APP_ADMIN_EMAIL")
APP_ADMIN_NAME = os.environ.get("APP_ADMIN_NAME")
