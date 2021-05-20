import os


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
