from typing import Union
from typing_extensions import Annotated

from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from contextlib import asynccontextmanager

from db.db import engine
from models.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/")
async def read_root(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}
