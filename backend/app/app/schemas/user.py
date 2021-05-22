from fastapi_users import models
from datetime import date
from pydantic import validator

class User(models.BaseUser):
    name: str
    surname: str
    phone_number: str
    birth_date: date

# TODO Maybe shit code
class UserCreate(models.BaseUserCreate):
    name: str
    surname: str
    phone_number: str
    birth_date: date
    @validator('phone_number')
    def validate_number(cls, v):
        if v[0] == '+':
            number = v[1:-1]
        else:
            number = v

        try:
            int(number)
            return number
        except:
            raise ValueError("Must contain only numbers")


class UserUpdate(User, models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    pass
