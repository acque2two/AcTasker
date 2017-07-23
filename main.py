#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask, jsonify

from config import CONFIG

# monkey.patch_all()

app = Flask(__name__)

app.config.from_object('config.CONFIG.FLASK.' + ('DEVELOPMENT' if CONFIG.DEV else "PRODUCTION"))

if __name__ == '__main__':


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

    # 肉ご飯
    app.run(host='0.0.0.0', port=29580)
    #
    # http_server = WSGIServer(('', app.config['PORT']), app,
    #                          environ={'wsgi.multithread': True})
    # http_server.serve_forever()
