#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import render_template

from AcTasker.web import web_root


@web_root.route("/")
def web_root_get():
    return render_template("index.html", **{"is_login": False})
