from flask import render_template,request
from flask.json import jsonify

from . import habits
from .models import Habit, habits_list

json = {'id':1,
    'name':'test',
    'description':'testeando',
    'days':2
    }
habito_test = Habit(**json)
habits_list.append(habito_test)


@habits.route('/create',methods=['POST'])
def create():
    try:
        n_habit = Habit(**request.json)
        habits_list.append(n_habit)
        print(habits_list)
    except:
        return '',405
    else:
        return '',200

@habits.route('/get',methods=['GET'])
def get():
    [print(i) for i in habits_list]
    return '',200

@habits.route('/delete/<int:id_h>',methods=['DELETE'])
def delete(id_h):
    for i in habits_list:
        if(i.id_h==id_h):
            habits_list.remove(i)
    [print(i) for i in habits_list]
    return '',200

@habits.route('/edit/<int:id_h>',methods=['PUT'])
def edit(id_h):
    for i in habits_list:
        if(i.id_h==id_h):
            i.changes(**request.json)
            print(i)
            return '',200
    return 'No se pudo',405
