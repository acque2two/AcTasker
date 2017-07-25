#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import render_template

from AcTasker.web.libs.auth import need_login
from AcTasker.web.web import web_root


@web_root.route("/tasks/add", methods=["GET"])
@need_login()
def web_tasks_add_get():
    return render_template("tasks/add.html",
                           **{"is_login": True, "menu": [{"name": "aaa", "id": "aaa", "type": "text"}]})
