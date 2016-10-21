

from flask_restful import Resource, reqparse


def get_fit_args():
    root_parser = reqparse.RequestParser()
    root_parser.add_argument('ship', type=int, required=True, location='form', help='Type ID for the ship being fit.')
    root_parser.add_argument('rig', type=list, location='form', help='')
    root_args = root_parser.parse_args(strict=True)

    return root_args


class EosResource(Resource):
    def post(self):
        args = get_fit_args()

        return {}, 200
