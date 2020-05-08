from flask import Blueprint

user_blue = Blueprint('user',__name__)

from app.User import loginModel

