from fastapi import FastAPI
from .database import engine, Base
from . import models
from .routers import tasks, users, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(tasks.router)

app.include_router(users.router)

app.include_router(authentication.router)