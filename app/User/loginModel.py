from app.User import user_blue
from flask import request,redirect,url_for,session
from exts import db
from models import User


# 处理登录
@user_blue.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter(User.Email == email,User.Password == password).first()
        if user:
            session['UserID'] = user.UserID
            return redirect(url_for('index'))
        else:
            return u'邮箱或密码错误，请确认重新填入'

# 处理注册
@user_blue.route('/regist/',methods=['GET','POST'])
def regist():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        password1 = request.form.get('password1')

        user = User.query.filter(User.Email == email).first()
        if user:
            return u'该邮箱已被注册，请您更换邮箱'
        else:
            if password != password1:
                return u'两次填写密码不相等，请重新填写'
            else:
                user = User(Email=email,Username=username,Password=password)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('index'))


@user_blue.context_processor
def my_context_processor():
    user_id = session.get('UserID')
    if user_id:
        user = User.query.filter(User.UserID == user_id).first()
        if user:
            return {'user': user}
        else:
            return {'user':User.query.filter(User.UserID == 1).first()}
    return {}