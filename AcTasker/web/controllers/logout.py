from flask import session, redirect

from AcTasker.web import web_root
from AcTasker.web.libs.auth import need_login


@need_login(no_redirect=False)
@web_root.route("/logout", methods=["GET"])
def web_logout_get():
    session.clear()
    return redirect("/")
