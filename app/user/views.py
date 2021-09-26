from flask import json, request,jsonify
from flask_jwt_extended import create_access_token,get_jwt_identity,jwt_required


from . import user
from .models import *
from .dbmodel import *

@user.route('/register',methods=['POST'])
def register():
    r=request.json
    username=r['username']
    name=r['name']
    password=r['password']
    user=User(username,name,password)
    userdb=Userdb().create_user(user)
    if(userdb):
        return 'Success',200
    return 'There is someone with that name',409


@user.route('/login',methods=['POST'])
def login():
    r=request.json
    username=r['username']
    password=r['password']
    user=User(username,password)
    userdb=Userdb().login(user)
    if(userdb):
        access_token = create_access_token(identity=user.username)
        return jsonify({'access_token':access_token,'username':user.username}),200
    return 'Access denied',401

@user.route('/password',methods=['POST'])
@jwt_required()
def change_password():
    current_user = get_jwt_identity()
    r=request.json
    old_password=r['old_password']
    new_password=r['new_password']
    userdb=Userdb().update_password(current_user,old_password,new_password)
    if(userdb):
        return 'Success',200
    return 'Error',401

@user.route('/username',methods=['POST','PUT'])
@jwt_required()
def change_username():
    current_user = get_jwt_identity()
    r=request.json
    new_username=r['username']
    userdb=Userdb().update_username(current_user,new_username)
    if(userdb):
        return 'Success',200
    return 'Access denied',401

