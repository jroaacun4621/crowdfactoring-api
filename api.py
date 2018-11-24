# External packages
from flask_restful import Api

from resources.check_resource import CheckResource
from resources.loans_resource import LoansResource
from resources.page_info_resource import PageInfoResource
from resources.user_resource import UserResource

def setup_api(app):
    api = Api(app)

    api.add_resource(CheckResource, '/')
    api.add_resource(LoansResource, '/loans/<user_id>')
    api.add_resource(PageInfoResource, '/pageInfo')
    api.add_resource(UserResource, '/user/<auth_id>')