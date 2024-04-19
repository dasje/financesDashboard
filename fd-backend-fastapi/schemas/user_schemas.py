from pydantic import BaseModel
from pydantic.functional_validators import AfterValidator
import re
from typing_extensions import Annotated, Union
from datetime import datetime

def validate_email(value):
    pattern = r'^[\w\-\.]+@([\w-]+\.)+[\w-]{2,}$'
    assert re.match(pattern, value), "Invalid email format."
    return value

def validate_password(value):
    min_max_length = r'^[\s\S]{8,32}$'
    upper = r'[A-Z]'
    lower = r'[a-z]'
    number = r'[0-9]'
    special = r'[ !"#$%&\'()*+,\-./:;<=>?@[\\\]^_`{|}~]'

    assert re.search(min_max_length, value), "Password is the wrong length."
    assert re.search(upper, value), "Password does not contain upper case character(s)." 
    assert re.search(lower, value), "Password does not contain lower case character(s)." 
    assert re.search(number, value), "Password does not contain digit(s)." 
    assert re.search(special, value), "Password does not contain special character(s)."
    return value


class User(BaseModel):
    email: Annotated[str, AfterValidator(validate_email)]
    password: Annotated[str, AfterValidator(validate_password)]

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    expires: int
    token_type: str
    

class TokenData(BaseModel):
    user_email: Union[str, None] = None

