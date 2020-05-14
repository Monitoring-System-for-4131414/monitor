from app.Warning import warning_blue
from flask import request,redirect,url_for,session,render_template
from exts import db
from models import Remain

class Warning(object):
    def __init__(self, type1, type2):
        self.type1 = type1
        self.type2 = type2
        self.state = 0
        self.title = [u'没有异常。', u'警告！']
        self.content = [u'今天没有监测到意外事故发生。', u'今天没有观测到陌生人员进入宿舍.', u'今天几时几分有陌生人员进入宿舍。', u'现在宿舍可能有意外发生。']

warnings = [Warning(0, 0), Warning(0, 1), Warning(1, 3)]

#预警信息
@warning_blue.route('/viewWarning')
def viewWarning():

    context = {
        'warningList':warnings
    }

    return render_template('warning.html',**context)

#信息确认
@warning_blue.route('/infConfirm/')
def infConfirm():
        warningType = request.args.get('c')
        Type = int(warningType)
        for w in warnings:
            if w.type2 == Type:
               w.state = 1

        return redirect(url_for('warning.viewWarning'))


