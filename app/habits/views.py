from flask import request
from flask.json import jsonify
from . import habits
from .models import Habit
from .dbmodel import Habitdb
import json
from bson import json_util
from flask_jwt_extended import get_jwt_identity,jwt_required


@habits.route('/',methods=['POST'])
@jwt_required()
def create():
    current_user = get_jwt_identity()
    habit = Habit(**request.json)
    new_habit=Habitdb().create_habit(habit,current_user)
    if(new_habit):
        return jsonify(request.json),200
    return 'Error',409

@habits.route('/',methods=['GET'])
@jwt_required()
def get():
    current_user = get_jwt_identity()
    habit_db=Habitdb().get_all_habits(current_user)
    response=json.loads(json_util.dumps(habit_db))
    return jsonify(response),200

@habits.route('/<string:_id>',methods=['DELETE'])
@jwt_required()
def delete(_id):
    habit_db=Habitdb().delete_habit(_id)
    if(habit_db):
        return 'Sucess',200
    return 'Cant delete it',409

@habits.route('/<string:_id>',methods=['PUT'])
@jwt_required()
def edit(_id):
    habit=Habitdb().get_habit_Object(_id)
    habit.changes(**request.json)
    habit_db=Habitdb().update_habit(habit)
    if(habit_db):
        return jsonify(request.json),200
    return 'Cant edit anything',405

@habits.route('/today/<string:_id>',methods=['POST'])
@jwt_required()
def marktoday(_id):
    r=request.json
    habit=Habitdb().get_habit_Object(_id)
    try:
        if(r['mark']):
            habit.date.mark_today()
        else:
            habit.date.unmark_today()
        update_habit=Habitdb().update_habit(habit)
        if(update_habit):
            return 'Sucess',200
    except KeyError:
        return 'error in date',405

