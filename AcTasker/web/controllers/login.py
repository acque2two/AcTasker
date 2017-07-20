#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import hashlib
import time

from flask import render_template, request, session, redirect

from AcTasker.db.schema import User
from AcTasker.web.web import web_root


@web_root.route("/login", methods=["GET"])
def web_login_get():
    return render_template("auth/login.html", **{"is_login": False})


@web_root.route("/login", methods=["POST"])
def web_login_post():
    user = User.objects().filter(auth__name__exact=request.form.get("name")).first()

    print([user.auth.name, user.auth.password])
    print([request.form.get("name"), request.form.get("password")])
    print(user.auth.salt)
    print(hashlib.sha512(
        (
            "%s:%s:%s" % (
                user.auth.salt, hashlib.md5(request.form.get("password", '').encode("UTF-8")).hexdigest(),
                user.auth.salt
            )
        ).encode("UTF-8")
    ).hexdigest())

    if user is None:
        return render_template("auth/login.html", **{"is_login": False, "is_failed": True})

    if user.auth.password == hashlib.sha512(
            (
                        "%s:%s:%s" % (
                            user.auth.salt, hashlib.md5(request.form.get("password", '').encode("UTF-8")).hexdigest(),
                            user.auth.salt
                    )
            ).encode("UTF-8")
    ).hexdigest():
        session["username"] = user.auth.name
        session["secret_key"] = hashlib.md5(
            ("%s%s%s" % (user.auth.salt, user.auth.name, user.auth.salt)).encode("UTF-8")).hexdigest()
        session["logined_datetime"] = int(time.mktime(datetime.datetime.now().timetuple()))

        return redirect("/usertop")

    return render_template("auth/login.html", **{"is_login": False, "is_failed": True})
