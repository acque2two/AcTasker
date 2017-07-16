#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import render_template

from AcTasker.web.web import web_root


@web_root.route("/login", methods=["GET"])
def web_login_get():
    return render_template("auth/login.html", **{"is_login": False})
