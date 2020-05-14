from flask import Blueprint

prompting_blue = Blueprint('prompting',__name__)

from app.Prompting import promptingModel