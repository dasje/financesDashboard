from typing import Union
from typing_extensions import Annotated

from fastapi import FastAPI, Depends, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from db.db import engine, get_db
from models.models import Base
from schemas.user_schemas import User
from api.login import sign_up_user, login_user

Base.metadata.create_all(bind=engine)

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/")
async def read_root(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}


@app.post("/sign_up", status_code=status.HTTP_201_CREATED, tags=['login'])
async def add_user(user: User) -> str:
    print("Validation passed at endpoint invocation.")
    return sign_up_user(user=user)


@app.get("/login", status_code=status.HTTP_201_CREATED, tags=['login'])
async def access_user(user: User):
    r = login_user(user=user)
    return JSONResponse(status_code=200, content=r.model_dump_json())