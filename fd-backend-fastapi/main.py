from typing_extensions import Annotated

from fastapi import FastAPI, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from db.db import engine
from models.models import Base
from schemas.user_schemas import User, Token
from schemas.response_schemas import BaseResponse
from api.login import sign_up_user, login_user 

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/sign_up", status_code=status.HTTP_201_CREATED, tags=['login'])
async def add_user(user: User) -> BaseResponse:
    return sign_up_user(user=user)


@app.post("/login", status_code=status.HTTP_201_CREATED, tags=['login'])
async def access_user(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],) -> Token:
    return login_user(form_data=form_data)