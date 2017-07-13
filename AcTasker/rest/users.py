from flask import Blueprint
from flask_restful import Api, Resource
from AcTasker.db import db

rest = Blueprint("rest_users", __name__)
api = Api(rest)




class User(Resource):
    def get(self):
        pass




api.add_resource(HelloWorld, '/')