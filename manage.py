from flask_script import Manager
from flask_migrate import Migrate , MigrateCommand
from monitor import app
from exts import db

manager = Manager(app)
#使用migrate绑定app和db
db.init_app(app)
migrate = Migrate(app,db)

#添加迁移脚本的命令到manager中

manager.add_command('db',MigrateCommand)

if __name__ == "__main__":
    manager.run()