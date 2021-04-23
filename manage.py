import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from run import create_app

config = os.environ['APP_SETTINGS']
app, db = create_app(config)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
