#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import session, redirect

from AcTasker.web.libs.auth import need_login
from AcTasker.web.web import web_root


@need_login(no_redirect=False)
@web_root.route("/logout", methods=["GET"])
def web_logout_get():
    session.clear()
    return redirect("/")
