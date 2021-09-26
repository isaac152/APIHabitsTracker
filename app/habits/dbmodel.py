from hashlib import new
from pymongo.message import query
from werkzeug.wrappers import response
from ..extensions import mongo
from bson.objectid import ObjectId
from .models import Habit

class Habitdb():
    def __init__(self,habit=Habit()):
        self.db=mongo.db.users
        self.habit=habit

    def exist_user(self,username):
        query={'username':username}
        response=self.db.users.find_one(query)
        if(response):
            return query
    def exist_habit(self,_id):
        query={'Habits._id':ObjectId(_id)}
        response=self.db.users.find_one(query)
        if(response):
            return response

    def get_all_habits(self,username):
        query=self.exist_user(username)
        if(query):
            document=self.db.users.find_one(query)
            return document['Habits']

    def format_habit(self,habit):
        if(not habit._id):
            habit._id=ObjectId()
        return {
            '_id':habit._id,
            'name':habit.name,
            'description':habit.description,
            'days':habit.days,
            'Marks':[i for i in habit.date.dates]
            }

    def create_habit(self,habit,username):
        query=self.exist_user(username)
        if(query):
            habit_format = self.format_habit(habit)
            response =self.db.users.update(query,
            {
                "$push":{
                   "Habits":habit_format
                    }
            })
            if(response['updatedExisting']):
                return habit_format['_id']
    def delete_habit(self,_id):
        query=self.exist_habit(_id)
        if(query):
            response= self.db.users.update(
                query,
                {"$pull":{
                    "Habits":{
                    "_id":ObjectId(_id)
                    }
                }
                }
            )
            return response['updatedExisting']
    
    def get_habit_elements(self,habits,_id):
        for i in habits:
            if(i['_id']==ObjectId(_id)):
                return i

    def get_habit_Object(self,_id):
        habit_query=self.exist_habit(_id)
        if(habit_query):
            habit=self.get_habit_elements(habit_query['Habits'],_id)
            return Habit(**habit)
            
    def update_habit(self,habit):
        if(habit):
            format_habit=self.format_habit(habit)
            response=self.db.users.update(
                {"Habits._id":ObjectId(habit._id)},
                {
                    "$set":{
                        "Habits.$":format_habit
                    }
                }
            )
            return response['updatedExisting']


