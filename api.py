# External packages
from flask_restful import Api

from resources.check_resource import CheckResource

def setup_api(app):
    api = Api(app)

    api.add_resource(CheckResource, '/')
