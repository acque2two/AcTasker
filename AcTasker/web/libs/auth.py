#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
from functools import wraps

from flask import session, redirect, g, request

from AcTasker.db.schema.users.user import User


def need_login(no_redirect=False, logined_redirect=None):
    def is_login(func):
        @wraps(func)
        def login(*args, **kwargs):
            print(request.path)
            g.username = session.get("username", None)
            if g.username == None:
                if no_redirect is False:
                    return redirect("/login")
                return func(*args, **kwargs)
            g.user = User.objects.filter(auth__name=g.username).first()
            print(g.user)
            if session.get('secret_key') == hashlib.md5(
                    ("%s%s%s" % (g.user.auth.salt, g.username, g.user.auth.salt)).encode("UTF-8")).hexdigest():
                if logined_redirect is not None:
                    return redirect(logined_redirect)
                return func(*args, **kwargs)
            else:
                print(no_redirect)
                if no_redirect is False:
                    return redirect("/login")
                return func(*args, **kwargs)

        return login

    return is_login
