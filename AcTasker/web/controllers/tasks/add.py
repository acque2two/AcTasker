#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import render_template

from AcTasker.web.web import web_root


@web_root.route("/tasks/add", methods=["GET"])
def web_tasks_add_get():
    return render_template("tasks/add.html", **{"is_login": False})
