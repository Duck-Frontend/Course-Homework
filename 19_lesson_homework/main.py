import os
from flask import Flask

from view.task import task_bp
from view.auth import auth_bp

app = Flask(__name__)


app.secret_key = os.urandom(24)


app.register_blueprint(task_bp)
app.register_blueprint(auth_bp)
