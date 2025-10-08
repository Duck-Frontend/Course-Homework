from flask import Blueprint, render_template, request, redirect
from controller.user import UserController as controller

auth_bp = Blueprint('auth', __name__, template_folder='templates/auth/')


@auth_bp.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("auth/register.html")
    elif request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        password_repeat = request.form["password_repeat"]

        result = controller.register(name, email, password, password_repeat)
        if result == "OK":
            return redirect("/")
        else:
            return "Fuck You"


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("auth/login.html")
    elif request.method == "POST":
        login = request.form["login"]
        password = request.form["password"]

        print(login, password)

        return redirect("/")
