#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import render_template

from AcTasker.web.web import web_root


@web_root.route("/tasks/list", methods=["GET"])
def web_tasks_list_get():
    return render_template("tasks/list.html", **{"is_login": False})
