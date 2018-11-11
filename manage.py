from app import app
from flask_script import Manager
from api import setup_api

manager = Manager(app)
setup_api(app)

if __name__ == "__main__":
    manager.run()