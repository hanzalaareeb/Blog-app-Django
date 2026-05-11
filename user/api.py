from ninja import Router
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from ninja.errors import HttpError
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .schemas import UserCreateSchema, UserResponseSchema, UserUpdateSchema, ChangePasswordSchema

router = Router()
User = get_user_model()

@router.post("/register/", response={201: UserResponseSchema}, auth=None)
def register(request, payload: UserCreateSchema):
    try:
        validate_password(payload.password)
    except ValidationError as e:
        raise HttpError(400, "; ".join(e.messages))
    
    try:
        user = User.objects.create_user(
            username=payload.email, # mapping email as username
            email=payload.email,
            password=payload.password,
            first_name=payload.first_name,
            last_name=payload.last_name,
        )
        return 201, user
    
    except IntegrityError:
        raise HttpError(409, "A user with this email already exists.")
    

@router.get("/me/", response=UserResponseSchema)
def update_profile(request, payload: UserUpdateSchema):
    user = request.auth
    if payload.first_name is not None:
        user.first_name = payload.first_name
    if payload.last_name is not None:
        user.last_name = payload.last_name
    user.save()
    
    if payload.organiization is not None:
        user.profile.organization = payload.organiization
        user.profile.save()
    
    return user

@router.post("/me/change_password/", response={200: dict})
def change_password(request, payload: ChangePasswordSchema):
    user = request.auth
    if not user.check_password(payload.current_password):
        raise HttpError(400, "Current password is incurrect.")
    
    try:
        validate_password(payload.new_password, user)
    except ValidationError as e:
        raise HttpError(400, "; ".join(e.messages))
    user.save()
    
    return {"detail": "password updated successfully."}
