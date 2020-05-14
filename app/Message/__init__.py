from flask import Blueprint

message_blue = Blueprint('message',__name__)

from app.Message import lookBackModel