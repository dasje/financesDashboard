from pydantic import BaseModel
from enum import Enum

class OutgoingMessage(str, Enum):
    user_added = "User added."
    user_exists = "User already exists."
    user_not_added = "User not added."


class BaseResponse(BaseModel):
    message: OutgoingMessage