from flask import Blueprint

habits = Blueprint('habits',__name__,url_prefix='/habits')

from . import views