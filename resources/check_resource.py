from flask_restful import Resource
from managers.page_info_manager import PageInfoManager
import json
class CheckResource(Resource):
    """
    Check API Endpoints
    """
    def get(self):
        """
        Return code to identify status of the api
        :return response: JSON. Ie, {}
        """
        Page_Info = PageInfoManager.get_id('1')
        print(Page_Info['id'])
        print(Page_Info['visits'])
        return "It's working " + json.dumps(Page_Info)