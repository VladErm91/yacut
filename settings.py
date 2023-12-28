import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY') 


MAX_SHORT_LINK_LENGHT = 16
ALLOWED_SYMBOLS = r'^[A-Za-z0-9]*$'
URL_SYMBOLS = r'^[a-z]+://[^\/\?:]+(:[0-9]+)?(\/.*?)?(\?.*)?$'