import datetime
class Config:
    SECRET_KEY = 'secreto'
    JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(days=7)
    