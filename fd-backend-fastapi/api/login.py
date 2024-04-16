
from datetime import datetime, timedelta, timezone
from typing import Annotated, Union

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext

from crud.general_crud import (
    add_item,
    get_item
)
from schemas.user_schemas import (
    User,
    Token,
    TokenData
)
from schemas.response_schemas import (
    BaseResponse,
    OutgoingMessage
)
from models.models import Users

from config import (
    SECRET_KEY,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    ALGORITHM,
)


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Use CryptContext to verify entered passport against stored hash.

    Args:
        plain_password (str):
        hashed_password (str):

    Returns:
        bool:
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Use CryptContext to generate a hash for the entered password.

    Args:
        password (str)

    Returns:
        str
    """
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None) -> str:
    """
    Generate an access token with expiry time.

    Args:
        data (dict)
        expires_delta (Union[timedelta, None], optional). Defaults to None.

    Returns:
        str
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def authenticate_user(email: str, password: str) -> Users:
    """
    Confirm user registered in db.
    Veryify entered password is correct.

    Args:
        email (str)
        password (str)

    Returns:
        Users
    """
    user = get_item(Users, [Users.email == email])
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> dict:
    """
    Args:
        token (Annotated[str, Depends)

    Raises:
        credentials_exception

    Returns:
        dict
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_email: str = payload.get("sub")
        if user_email is None:
            raise credentials_exception
        token_data = TokenData(user_email=user_email)
    except JWTError:
        raise credentials_exception
    user = get_item(Users, [Users.email == token_data.user_email])
    if user is None:
        raise credentials_exception
    return user


def sign_up_user(user: User) -> BaseResponse:
    """
    If user details passed schema validations, add user to 'user' table in database.

    Args:
        user (User)

    Returns:
        str
    """
    user_exists = get_item(Users, [Users.email == user.email])
    if user_exists:
        raise HTTPException(400, detail=OutgoingMessage.user_exists.value)
    
    user_to_insert = Users()
    user_to_insert.email = user.email
    user_to_insert.hashed_password = get_password_hash(user.password)
    user_to_insert.sign_up_date = datetime.now()

    new_user = add_item(user_to_insert)
    if new_user == user_to_insert:
        return BaseResponse(message=OutgoingMessage.user_added.value)
    return HTTPException(500, detail=OutgoingMessage.user_not_added.value)

    
def login_user(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> BaseResponse:
    """
    Args:
        form_data (Annotated[OAuth2PasswordRequestForm, Depends)

    Raises:
        HTTPException

    Returns:
        BaseResponse
    """
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")