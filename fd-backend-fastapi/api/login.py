from schemas.user_schemas import User
from schemas.response_schemas import BaseResponse
from models.models import Users
from passlib.context import CryptContext
from datetime import datetime
from crud.general_crud import add_item, get_item

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

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
        return BaseResponse(message="User already exists.")
    
    user_to_insert = Users()
    user_to_insert.email = user.email
    user_to_insert.hashed_password = pwd_context.hash(user.password)
    user_to_insert.sign_up_date = datetime.now()

    new_user = add_item(user_to_insert)
    if new_user == user_to_insert:
        return BaseResponse(message="User added.")
    return BaseResponse(message="User not added.")

    
def login_user(user: User) -> BaseResponse:
    if user.email:
        r = BaseResponse(message="Email correct.")
        return r
    else:
        r = BaseResponse(message="No valid email.")
        return r