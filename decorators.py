
from functools import wraps
from flask import session ,redirect ,url_for

def login_required(func):

    @wraps(func)
    def wrapper(*args,**kwargs):
        if(session.get('UserID')):
            return func(*args,**kwargs)
        else:
            return redirect(url_for('index'))
