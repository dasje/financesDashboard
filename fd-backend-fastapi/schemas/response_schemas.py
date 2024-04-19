from pydantic import BaseModel
from enum import Enum

class OutgoingMessage(str, Enum):
    user_added = "User added."
    user_exists = "User already exists."
    user_not_added = "User not added."
    user_detail_incorrect = "Incorrect email or password."


class BaseResponse(BaseModel):
    message: OutgoingMessage