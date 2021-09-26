import datetime
class Config:
    SECRET_KEY = 'dont know, what about, mickey mouses?'
    JWT_SECRET_KEY= "mizkamuzka mickey mouse ?"
    JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(days=7)
    JWT_ACCESS_TOKEN_EXPIRES=datetime.timedelta(hours=1)

    MONGO_URI = "Your uri her"