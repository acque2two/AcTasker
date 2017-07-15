import hashlib
from functools import wraps

from flask import session, redirect

from AcTasker.db.schema.users.user import User


def need_login(no_redirect=False):
    def is_login(func):
        @wraps(func)
        def login(*args, **kwargs):
            g.username = session.get("username")
            g.user = User.objects(auth__name=g.username)
            if session.get('secret_key') == hashlib.md5("%s%s%s" % (g.user.auth.salt, g.username, g.user.auth.salt)):
                return func
            else:
                if no_redirect:
                    return func
                return redirect("/login")

        return login

    return is_login
