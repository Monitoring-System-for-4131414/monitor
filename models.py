from exts import db

class User(db.Model):
    __tablename__ = 'user'
    UserID = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    Username = db.Column(db.String(125), nullable=True)
    Password = db.Column(db.String(125), nullable=False)
    Sex = db.Column(db.String(10), nullable=True)
    Username = db.Column(db.String(125), nullable=True)
    DormitoryID = db.Column(db.String(125), nullable=True)
    Phone = db.Column(db.String(125), nullable=True)
    Email = db.Column(db.String(125), nullable=True)
    CallMethod = db.Column(db.String(3), nullable=True)

class Dormitory(db.Model):
    __tablename__ = 'dormitory'
    dormitoryid = db.Column(db.String(125), primary_key=True, nullable=True)
    dormitoryname = db.Column(db.String(125), nullable=False)

class Remain(db.Model):
    __tablename__ = 'remain'
    remindid = db.Column(db.String(125), primary_key=True)
    time = db.Column(db.String(20), nullable=True)
    type = db.Column(db.String(3), nullable=True)
    content = db.Column(db.String(255), nullable=False)

class Remain_Log(db.Model):
    __tablename__ = 'remain_log'
    remindid = db.Column(db.String(125), primary_key=True, nullable=True)
    time = db.Column(db.String(20),primary_key=True, nullable=True)
    type = db.Column(db.String(3), nullable=True)
    content = db.Column(db.String(255), nullable=False)

class Envirment(db.Model):
    __tablename__ = 'envirment'
    dormitoryid = db.Column(db.String(125), primary_key=True, nullable=True)
    temperature = db.Column(db.Float(10), nullable=False)
    humidity = db.Column(db.Float(10), nullable=False)
    time = db.Column(db.TIMESTAMP(20), nullable=False)

class Vedio(db.Model):
    __tablename__ = 'vedio'
    vedioid = db.Column(db.String(125), nullable=True, primary_key=True)
    dormitoryid = db.Column(db.String(125), db.ForeignKey('dormitory.dormitoryid'),nullable=True)
    vediobegin = db.Column(db.TIMESTAMP(20), nullable=True)
    vedioend = db.Column(db.TIMESTAMP(20), nullable=True)
    path = db.Column(db.String(255), nullable=True)
