#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import datetime
import hashlib
import random
import string

from flask import render_template, request, session

from AcTasker.db.schema.users.auth import Auth
from AcTasker.db.schema.users.info import Info
from AcTasker.db.schema.users.user import User
from AcTasker.web.libs.error import Error
from AcTasker.web.web import web_root


@web_root.route("/signup", methods=["GET"])
def web_signup_get():
    return render_template("auth/signup.html", **{"is_login": False, "user": {"email": '', 'uid': '', 'password': ''}})


@web_root.route("/signup", methods=["POST"])
def web_signup_post():
    if request.form.get("checked", None) == "OK":
        if request.form.get["hash"] != session.get("hash"):
            Error.bad_request(detail="不正な手順での操作が行われました。")
        user = User()
        user.auth = Auth()
        user.auth.name = session["uid"]
        user.auth.salt = session["salt"]
        user.auth.email = session["email"]
        user.auth.password = session["password"]
        user.auth.updated_date = datetime.datetime.now()
        user.auth.save()
        user.info = Info()

        user.save()

    user = {"email": request.form.get("email", None), "uid": request.form.get("uid", None),
            "salt":  ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(48)])
            }

    user["password"] = hashlib.sha512(
        (
            "%s:%s:%s" % (
                user["salt"], request.form.get("password", None), user["salt"]
            )
        ).encode("UTF-8")
    ).hexdigest()

    user["hash"] = hashlib.md5(
        ("%s:%s:%s:%s:%s:%s:%s" % (
            user['salt'], user['email'], user['salt'], user['uid'], user['salt'], user['password'], user['salt']
        )).encode("UTF-8")
    ).hexdigest()

    session['userdata'] = user
    session["csrf_token"] = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(64)])

    print(user)
    return render_template("auth/signup.html", **{
        "is_login":          False,
        "user":              user,
        'checked':           True,
        "csrf_token": session["csrf_token"]
    })
