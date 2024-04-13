from typing import Union
from typing_extensions import Annotated

from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/")
async def read_root(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}
