from flask import Blueprint, render_template

web_root = Blueprint("web_root", __name__, template_folder="templates")


@web_root.route("/")
def web_root_get():
    return render_template("index.html", **{"is_login": False})
