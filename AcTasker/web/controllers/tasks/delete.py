#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import render_template

from AcTasker.web.web import web_root


@web_root.route("/tasks/delete", methods=["GET"])
def web_tasks_delete_get():
    return render_template("tasks/delete.html", **{"is_login": False})
