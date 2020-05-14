from flask import Flask,render_template, session,redirect,url_for,request
import config
from exts import db
from app.User import user_blue
from models import User

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

app.register_blueprint(user_blue)
# 进入主页
@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html', UserID=session.get('UserID'))

@app.route('/member/',methods=['GET','POST'])
def member():
    user_id = session.get('UserID')
    user = User.query.filter(User.UserID == user_id).first()

    if user:
        username = user.Username
        useremail = user.Email
        data = {
            "username": username,
            "useremail": useremail
        }

        return render_template('member.html',data = data)
    else:
        return redirect('/')

@app.route('/changemember/',methods=['GET','POST'])
def changemember():
    user_id = session.get('UserID')
    user = User.query.filter(User.UserID == user_id).first()

    username = user.Username
    sex = user.Sex
    phone = user.Phone
    dormitoryid = user.DormitoryID
    useremail = user.Email
    CallMethod = user.CallMethod
    data = {
        "username": username,
        "sex": sex,
        "phone": phone,
        "dormitoryid": dormitoryid,
        "email": useremail,
        "CallMethod":CallMethod
    }

    if request.method == "GET":
        return render_template('changemember.html', data=data)
    else:
        changename = request.form.get('username')
        changepassword = request.form.get('password')
        changesex = request.form.get('sex')
        changephone = request.form.get('phone')
        changedormitoryid = request.form.get('dormitoryid')
        changeemail = request.form.get('email')
        changeQQ = request.form.get('QQ')
        ChangeCallMethod = request.form.get('CallMethod')

        changedata = {
            "username": changename,
            "sex": changesex,
            "phone": changephone,
            "dormitoryid": changedormitoryid,
            "useremail": changeemail,
            "QQ": changeQQ,
            "CallMethod": ChangeCallMethod
        }


        user.Username = changename
        user.Password = changepassword
        user.Sex = changesex
        user.DormitoryID = changedormitoryid
        user.Phone = changephone
        user.Email = changeemail
        user.CallMethod = ChangeCallMethod
        db.session.commit()

        return render_template('member.html',data = changedata)


# 进入信息查看界面
@app.route('/viewPlayback')
def viewPlayback():
    return render_template('information_playback.html')

# 进入课表查看界面
@app.route('/viewTimetable')
def viewTimeTable():
    return  render_template('timetable.html')

@app.context_processor
def my_context_processor():
    user_id = session.get('UserID')
    if user_id:
        user = User.query.filter(User.UserID == user_id).first()
        if user:
            return {'user': user}
        else:
            return {'user':User.query.filter(User.UserID == 1).first()}
    return {}
if __name__ == '__main__':
    app.run()
