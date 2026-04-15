from ninja import Schema
from pydantic import EmailStr

class UserCreateSchema(Schema):
    email: EmailStr
    password: str
    first_name: str = ""
    last_name: str = ""
    
class UserResponseSchema(Schema):
    id: int
    email: str
    role: str
        