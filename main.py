from typing import List
from fastapi import FastAPI, Depends, Response, status, HTTPException

from blog.routes import authentication
from . import schemas, models
from .database import engine, get_db
from sqlalchemy.orm import Session
from .hashing import Hash
from .routes import blog, user

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(router=authentication.router)
app.include_router(router=blog.router)
app.include_router(router=user.router)


