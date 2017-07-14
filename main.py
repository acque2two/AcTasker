import traceback

from flask import Flask, jsonify
from gevent import monkey, signal

from config import CONFIG

monkey.patch_all()

app = Flask(__name__)

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




    @app.route('/check', methods=["GET"])
    def get_check():
        return jsonify({"status": "ok"})



    print("SERVER START...")

    if CONFIG.MODE == CONFIG.MODE_LIST.WEB:
        from AcTasker.web import web

        app.register_blueprint(web.web_root)
    else:
        print("Only supported WEB Mode")
        exit(-1)

    app.run(host='0.0.0.0', port=29580)
    #
    # http_server = WSGIServer(('', app.config['PORT']), app,
    #                          environ={'wsgi.multithread': True})
    # http_server.serve_forever()
