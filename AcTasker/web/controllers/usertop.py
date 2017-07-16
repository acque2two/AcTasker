#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import render_template

from AcTasker.web.web import web_root


@web_root.route("/usertop", methods=["GET"])
def web_usertop_get():
    return render_template("usertop.html", **{"is_login": False})
