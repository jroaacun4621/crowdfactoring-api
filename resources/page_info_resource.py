from flask_restful import Resource
from flask import jsonify

from controllers.page_info_controller import PageInfoController

class PageInfoResource(Resource):
    def get(self):
        return jsonify({
            'data': {
                'page_info': PageInfoController.get_id('1')
            }
        })

    def post(self):
        PageInfoController.increase_visits('1')