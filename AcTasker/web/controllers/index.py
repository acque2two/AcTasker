#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import render_template

from AcTasker.web.libs.auth import need_login
from AcTasker.web.web import web_root


@web_root.route("/")
@need_login(no_redirect=True, logined_redirect="/usertop")
def web_root_get():
    return render_template("index.html", **{"is_login": False})
