import json
import datetime
import os

from flask import Flask, session, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS as cors
from env import SimpleEnvLoader

from config import Config


app = Flask(__name__)
app.config.from_object(Config)

app.permanent_session_lifetime = datetime.timedelta(minutes=int(600000))
env = SimpleEnvLoader(os.path.dirname(__file__)).create_environment_variables()


@app.before_request
def make_session_permanent():
    session.permanent = True


database = SQLAlchemy(app)
application_cors = cors(app)

app.secret_key = "983mkjc89eic9ic"
app.config.update(SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=True)


@app.route("/current/user")
def get_current_user():
    print(request.cookies)
    data = session.get("user")
    if not data:
        return jsonify(status=400, message="No users")
    return json.loads(data)
