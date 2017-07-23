#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import datetime
import hashlib
import random
import re
import string

from flask import render_template, request, session, redirect

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

        print([user.auth.name, user.auth.password])
        print([request.form.get("uid"), request.form.get("password")])
        print([session.get("uid"), session.get("password")])
        return redirect("/login?signup_success=True")
    error = []

    user = {"email":        request.form.get("email", None), "uid": request.form.get("uid", None),
            "salt":         ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(48)]),
            "first_name":   request.form.get("first_name", None),
            "last_name":    request.form.get("last_name", None),
            "display_name": request.form.get("display_name", None),
            "password":     request.form.get("password", '')
            }

    if len(user["password"]) < 8:
        error.append("password_few")

    lowcase = re.search(r"[a-z]", request.form.get('password', '')) is not None
    upcase = re.search(r"[A-Z]", request.form.get('password', '')) is not None
    digit = re.search(r"\d", request.form.get("password", '')) is not None

    if not (lowcase and upcase and digit):
        error.append("password_weak")

    if len(User.objects(auth__email=user["email"]).all()) > 0:
        error.append("email_exist")

    if len(User.objects(auth__name=user["uid"]).all()) > 0:
        error.append("uid_exist")

    if len(error) > 0:
        user["password"] = ""
        return render_template("auth/signup.html", **{
            "is_login": False,
            "user":     user,
            'checked':  False,
            'error':    error
        })

    user["password"] = hashlib.sha512(
        (
            "%s:%s:%s" % (
                user["salt"], hashlib.md5(request.form.get("password", '').encode("UTF-8")).hexdigest(), user["salt"]
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
