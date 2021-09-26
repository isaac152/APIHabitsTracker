from pymongo.message import query
from ..extensions import mongo
from bson.objectid import ObjectId
from .models import User

class Userdb():
    
    def __init__(self):
        self.db=mongo.db.users

    def create_user(self,user):
        if(not self.check_user(user)):
            return self.db.users.insert_one(self.format_user(user))

    def login(self,user):
        user_db=self.get_user_by_username(user.username)
        if(user_db):
            if(user.check_password(user_db['password'])):
                return ObjectId((user_db['_id']))

    def format_user(self,user):
        return {
            'username':user.username,
            'name':user.name,
            'password':user.password
        }
    def update_username(self,username,update):
        if(self.get_user_by_username(username) and not (self.get_user_by_username(update))):
            query={'username':username}
            change={"username":update}
            response=self.db.users.update(query,{"$set":change})
            return response['updatedExisting']
        return False

    def update_password(self,username,old_password,new_password):
        userdb=self.get_user_by_username(username)
        if(userdb):
            user_pass=userdb['password']
            user = User('',old_password)
            if(user.change_password(user_pass,new_password)):
                query={'username':username}
                change={"password":user.password}
                response=self.db.users.update(query,{"$set":change})
                return response['updatedExisting']
        return False
    def get_user_by_id(self,id):
        return self.db.users.find_one({'_id':ObjectId(id)})

    def get_user_by_username(self,user):
        return self.db.users.find_one({'username':user})

    def check_user(self,user):
        return self.get_user_by_username(user.username)
