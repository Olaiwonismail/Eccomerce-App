
import os
class Config:
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///sqlite.db'
    SECRET_KEY='b30bb8384e15acbc267f8cb0f1b94c84'
    MAIL_SERVER='smtp.gmail.com'
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"
    SQLALCHEMY_DATABASE_URI =  os.getenv('SQLALCHEMY_DATABASE_URI')
    