import os
from fastapi_mail import ConnectionConfig

# Database config
POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_HOST = os.environ['POSTGRES_HOST']
POSTGRES_PORT = os.environ['POSTGRES_PORT']
POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
POSTGRES_DB = os.environ['POSTGRES_DB']

SQLALCHEMY_DATABASE_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# App config
PROJECT_NAME = "Musicurses"
MAIN_DEVELOPER = "Elisey Kravchuk (https://github.com/Udsh1n)"
SECRET = os.environ["SECRET"]
JWT_LIFETIME_SECONDS = 3600

# E-mail config
EMAIL_LOGIN = os.environ['EMAIL_LOGIN']
EMAIL_PASSWORD = os.environ['EMAIL_PASSWORD']
EMAIL_PROVIDER_URl = os.environ['EMAIL_PROVIDER_URl']

conf = ConnectionConfig(
    MAIL_USERNAME="Musicurses",
    MAIL_PASSWORD=EMAIL_PASSWORD,
    MAIL_FROM=EMAIL_LOGIN,
    MAIL_PORT=587,
    MAIL_SERVER=EMAIL_PROVIDER_URl,
    MAIL_FROM_NAME="Musicurses",
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True
)

# Cors origins
origins = [
    "*"
]
