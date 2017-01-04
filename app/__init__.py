import imp, sys
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

from flask import Flask, jsonify, request
from flask_login import current_user
from app.secret import *
from flask_sqlalchemy import SQLAlchemy

import json

app = Flask(__name__)
app.config.from_object('app.configure')
db = SQLAlchemy(app)

from app.Controller import init_controller
from app.Model import init_db
from app.login import init_login
from app.admin import init_admin

init_db()
init_controller(app)
init_login(app)
init_admin(app)