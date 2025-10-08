from flask import Blueprint, render_template, request, redirect


task_bp = Blueprint('task', __name__, template_folder='templates/todo')


@task_bp.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if request.method == "GET":
        return render_template("todo/add.html")

    elif request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]

        print(title, description)
        return redirect('/')
