from flask imprt Flask, render_template, request
from flask_session import Session

app = Flask("__name__")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"