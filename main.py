from routes.authentication.users_routes import router as users_router
from routes.authentication.groups_routes import router as groups_router
from routes.authentication.passwords_routes import router as passwords_router
from fastapi import FastAPI
from configs import settings as cfg
import services


app = FastAPI(
    title=cfg.APP_NAME,
    description=cfg.APP_DESCRIPTION,
    contact={
        "name": cfg.APP_AUTHOR,
        "email": cfg.APP_EMAIL,
    },
    version=cfg.APP_VERSION)

app.include_router(users_router)
app.include_router(groups_router)
app.include_router(passwords_router)
