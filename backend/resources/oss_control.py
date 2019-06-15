from backend.models.db_models import API
from flask_restful import reqparse
import werkzeug.datastructures
from backend.utils.oss import auth, bucket


class UploadDocuments(API):
    """
    上传到oss存储
    """

    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('data', type=werkzeug.datastructures.FileStorage, location='files')
        args = parse.parse_args()
        print(args)
