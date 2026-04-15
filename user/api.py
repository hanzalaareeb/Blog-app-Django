from ninja import Router
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from ninja.errors import HttpError
from .schemas import UserCreateSchema, UserResponseSchema

router = Router()
User = get_user_model()

# auth=None is the ninja equivalent f DRF's AllowAny
@router.post("/register/", response={201: UserResponseSchema}, auth=None)
def register_user(request, payload: UserCreateSchema):
    try:
        # User create_user to properly hash the password
        user = User.objects.create_user(
            username=payload.email, # mapping email as username
            email=payload.email,
            password=payload.password,
            first_name=payload.first_name,
            last_name=payload.last_name
        )
        return 201, user
    
    except IntegrityError:
        # Catch error if the user email already exists
        raise HttpError(400, "A user with this email already exists.")
    