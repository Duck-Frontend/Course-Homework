from flask import Flask, render_template

from view.task import task_bp
from view.auth import auth_bp

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


app.register_blueprint(task_bp)
app.register_blueprint(auth_bp)
