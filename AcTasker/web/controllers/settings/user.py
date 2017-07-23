#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib
import random
import string

from flask import render_template, g, request, session

from AcTasker.web.libs.auth import need_login
from AcTasker.web.libs.error import Error
from AcTasker.web.web import web_root


@web_root.route("/settings/user", methods=["GET"])
@need_login(no_redirect=False)
def web_settings_user_get():
    return render_template("settings/user.html", **{"is_login": True, "user": g.user})


@web_root.route("/settings/user", methods=["POST"])
@need_login(no_redirect=False)
def web_settings_user_post():
    if request.form.get('checked', False):
        if session.get('csrf_token', '') != request.form.get('csrf_token'):
            return Error.bad_request("Illegal Access", "不正な手順でアクセスされました")

    user = {
        "last_name":    request.form.get("last_name", None),
        "first_name":   request.form.get("first_name", None),
        "display_name": request.form.get("display_name", None)
    }
    user['hash'] = hashlib.md5('%s:%s:%s' % (user['last_name'], user['first_name'], user['display_name']))

    session["csrf_token"] = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(64)])

    return render_template("settings/user.html", **{"is_login": True, "user": user, 'checked': True})
