from fastapi import APIRouter, Request, BackgroundTasks, Response, Depends
from app.logic.auth.backends import jwt_authentication, fastapi_users
from app.core.config import SECRET, conf
from app.schemas.user import UserDB
from app.email.send import send_message
from fastapi_mail import FastMail, MessageSchema
from app.email.templates import verify, reset_password


router = APIRouter()

# Auth router with verification
router.include_router(
    fastapi_users.get_auth_router(
        jwt_authentication,
        requires_verification=True
        ),
    prefix="/auth/jwt",
    tags=["Auth"],
)

# Register router
router.include_router(
    fastapi_users.get_register_router(),
    prefix="/auth",
    tags=["Auth"],
)

# Verify router
async def after_verification_request(user: UserDB,
    token: str, 
    request: Request
    ):

    message = MessageSchema(
        subject="Musicurses verify account",
        recipients=[str(user.email)],
        body=verify.message.format(f"{user.name} {user.surname}", token),
        subtype="html"
        )

    fm = FastMail(conf)
    await fm.send_message(message)


router.include_router(
    fastapi_users.get_verify_router(SECRET, after_verification_request=after_verification_request),
    prefix="/auth",
    tags=["Auth"],
)


# Password reset
async def on_after_forgot_password(user: UserDB, token: str, request: Request):
    message = MessageSchema(
        subject="Musicurses reset password",
        recipients=[str(user.email)],
        body=reset_password.message.format(f"{user.name} {user.surname}", token),
        subtype="html"
        )
    fm = FastMail(conf)
    await fm.send_message(message)

router.include_router(
    fastapi_users.get_reset_password_router(SECRET, after_forgot_password=on_after_forgot_password),
    prefix="/auth",
    tags=["Auth"],
)


# JWT refresh token
@router.post("/auth/jwt/refresh", tags=['Auth'])
async def refresh_jwt(response: Response, user=Depends(fastapi_users.get_current_active_user)):
    return await jwt_authentication.get_login_response(user, response)
