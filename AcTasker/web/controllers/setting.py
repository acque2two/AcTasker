#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import render_template, g

from AcTasker.web.libs.auth import need_login
from AcTasker.web.web import web_root


@web_root.route("/settings", methods=["GET"])
@need_login(no_redirect=False)
def web_setting_get():
    return render_template("setting.html", **{"is_login": True, "user": g.user})
