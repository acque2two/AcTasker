import traceback

from flask import Flask, g, jsonify as flask_jsonify, request, jsonify
from gevent import monkey, signal
from gevent.pywsgi import WSGIServer

from config import CONFIG

monkey.patch_all()

app = Flask(__name__)
from AcTasker.db.db import db

app.config.from_object('config.CONFIG.FLASK.' + 'DEVELOPMENT' if CONFIG.DEV else "PRODUCTION")

if __name__ == '__main__':

    def got_signal(signum, frame):
        print("[!!SIGNAL!!]")
        traceback.print_stack()
        print(frame)
        import time
        time.sleep(2)
        exit()


    signal.signal(signal.SIGTERM, got_signal)


    # ----- REQUEST BEFORE AND AFTER -----1
    @app.before_request
    def db_init():
        g.db = db.session


    @app.teardown_request
    @app.errorhandler(500)
    def db_close(exception):
        if request.path in ('/healthz', '/', '/check'):
            return
        if exception:
            return 'Sorry', 500
        g.db.remove()


    print("SERVER STARTING...")


    @app.route('/check', methods=["GET"])
    def get_check():
        return jsonify({"status": "ok"})


    @app.route('/healthz')
    def healthz():
        return "OK"


    print("SERVER START...")
    # app.run(host='0.0.0.0', port=app.config['PORT'])

    http_server = WSGIServer(('', app.config['PORT']), app,
                             environ={'wsgi.multithread': True})
    http_server.serve_forever()
