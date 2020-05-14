from app.Message import message_blue
from flask import request,redirect,url_for,session,render_template
from exts import db
from models import Vedio


# 进入信息查看界面
@message_blue.route('/viewPlayback')
def viewPlayback():
    vedios = Vedio.query.all()
    return render_template('information_playback.html',vedios=vedios)


# 处理登录
@message_blue.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        # # user = User.query.filter(User.Email == email,User.Password == password).first()
        # if user:
        #     session['UserID'] = user.UserID
        #     return redirect(url_for('index'))
        # else:
        #     return u'邮箱或密码错误，请确认重新填入'
