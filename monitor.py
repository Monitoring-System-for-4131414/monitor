from flask import Flask,render_template, session,url_for,request,redirect
import config
from exts import db
from app.User import user_blue
from app.Warning import warning_blue
from app.Prompting import prompting_blue
from models import User,Remain

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

app.register_blueprint(user_blue)
app.register_blueprint(warning_blue)
app.register_blueprint(prompting_blue)


# 进入主页
@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html', UserID=session.get('UserID'))

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
