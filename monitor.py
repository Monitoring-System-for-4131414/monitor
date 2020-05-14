from flask import Flask,render_template, session
import config
from exts import db
from app.User import user_blue
from app.Message import message_blue
from models import User
from decorators import login_required

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

app.register_blueprint(user_blue)
app.register_blueprint(message_blue)
# 进入主页
@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html', UserID=session.get('UserID'))

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
