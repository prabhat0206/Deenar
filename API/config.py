from dotenv import load_dotenv
from os import environ
load_dotenv()

SQLALCHEMY_DATABASE_URI = environ.get('SQL_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = environ.get('SECRET_KEY')
ADMIN_EMAIL = environ.get('ADMIN_USERNAME')
ADMIN_PASSWORD = environ.get('ADMIN_PASSWORD')
TOKEN = environ.get('TOKEN')