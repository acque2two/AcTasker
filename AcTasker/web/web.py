from flask import Blueprint, render_template

from AcTasker.web.libs.error import Error

web_root = Blueprint("web_root", __name__, template_folder="templates")


@web_root.route("/")
def web_root_get():
    return Error.forbidden("気分", "そんな感じ")
    return render_template("error.html", **{"is_login": False})
