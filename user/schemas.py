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
    first_name: str = ""
    last_name: str = ""
    role: str
    
class UserUpdateSchema(Schema):
    first_name: str | None = None
    last_name: str | None = None
    organiization: str | None = None
    
class ChangePasswordSchema(Schema):
    current_password: str
    new_password: str
