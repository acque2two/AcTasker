# Base
import os
from socket import gethostname

# Flask
from flask import Blueprint, jsonify
from flask_restful import Api, Resource

rest = Blueprint("rest_server_status", __name__)
api = Api(rest)


class Status(Resource):
    def get(self):
        st = os.statvfs('/')
        return jsonify({
            'loadavg':  os.getloadavg(),
            'hostname': gethostname(),
            'inode':    {
                'used':       ((st.f_blocks - st.f_bfree) * st.f_frsize) / 1024,
                'free':       (st.f_bavail * st.f_frsize) / 1024,
                'total':      (st.f_blocks * st.f_frsize) / 1024,
                'percentage': (((st.f_blocks - st.f_bfree) * st.f_frsize) / 1024) / ((st.f_blocks * st.f_frsize) / 1024)
            }
        })



