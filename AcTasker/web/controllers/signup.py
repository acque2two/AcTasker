#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import datetime
import hashlib
import random
import string

from flask import render_template, request, session

from AcTasker.db.schema import Setting
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
    if request.form.get("checked", False):
        print("JOINING")
        if request.form.get("hash", "HOGE") != session.get("hash"):
            print("ABORT")
            return Error.bad_request(detail="不正な手順での操作が行われました。")
        user = User()
        user.auth = Auth()
        user.auth.name = session["user_data"]["uid"]
        user.auth.salt = session["user_data"]["salt"]
        user.auth.email = session["user_data"]["email"]
        user.auth.password = session["user_data"]["password"]
        user.auth.updated_date = datetime.datetime.now()
        user.auth.save()
        user.info = Info()
        user.info.first_name = session["user_data"]["first_name"]
        user.info.last_name = session["user_data"]["last_name"]
        user.info.display_name = session["user_data"]["display_name"]
        user.info.save()
        user.setting = Setting()
        user.setting.save()
        user.created_date = datetime.datetime.now()
        user.save()

        return render_template("auth/login.html", signup_success=True)

    user = {"email":        request.form.get("email", None), "uid": request.form.get("uid", None),
            "salt":         ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(48)]),
            "first_name":   request.form.get("first_name", None),
            "last_name":    request.form.get("last_name", None),
            "display_name": request.form.get("display_name", None)
            }

    user["password"] = hashlib.sha512(
        (
            "%s:%s:%s" % (
                user["salt"], request.form.get("password", None), user["salt"]
            )
        ).encode("UTF-8")
    ).hexdigest()

    user["hash"] = hashlib.md5(
        user["salt"].join([
            user['email'],
            user['uid'],
            user['password'],
            user['first_name'],
            user['last_name'],
            user['display_name']
        ]
        ).encode("UTF-8")
    ).hexdigest()

    session['user_data'] = user
    session['hash'] = user["hash"]
    session["csrf_token"] = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(64)])

    print(user)
    return render_template("auth/signup.html", **{
        "is_login":          False,
        "user":              user,
        'checked':           True,
        "csrf_token": session["csrf_token"]
    })
