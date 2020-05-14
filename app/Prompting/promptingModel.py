from app.Prompting import prompting_blue
from flask import request,redirect,url_for,session,render_template
from exts import db
from models import Remain

class Prompting(object):
    def __init__(self, type1, type2):
        self.type1 = type1
        self.type2 = type2
        self.state = 0
        self.title = [u'暂无注意事项。', u'注意！']
        self.content = [u' 今天还没有需要提醒信息。', u'宿舍卫生指数不达标，请尽快打扫。', u'宿舍过于吵闹，请保持安静。', u'宿舍目前没人，电源应该关闭。']

promptings = [Prompting(0, 0), Prompting(1, 1), Prompting(1, 3)]

#提示信息
@prompting_blue.route('/viewPrompting')
def viewPrompting():

    context = {
        'promptingList':promptings
    }

    return render_template('prompting.html',**context)

#信息确认
@prompting_blue.route('/infConfirm2/')
def infConfirm2():
    promptingType = request.args.get('b')
    Type = int(promptingType)
    for p in promptings:
        if p.type2 == Type:
           p.state = 1

        return redirect(url_for('prompting.viewPrompting'))