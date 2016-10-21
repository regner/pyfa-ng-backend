

from flask_restful import Resource


class FitsResource(Resource):
    def get(self):
        return {"fits": []}
