from flask import Blueprint
from flask_restful import Api, Resource

from AcTasker.rest.rest import rest

api = Api(rest)


class Users(Resource):
    children = Blueprint("rest_users", rest)
    users = Blueprint("rest_users", __name__)

    def get(self):
        return "404", 404
