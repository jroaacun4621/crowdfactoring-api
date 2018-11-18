from app import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from api import setup_api

manager = Manager(app)
setup_api(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.command
def create_database():
    db.create_all()

if __name__ == "__main__":
    manager.run()