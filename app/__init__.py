# -*- coding: utf-8 -*-

import imp, sys
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

from flask import Flask, jsonify, request, url_for
from flask_login import current_user
from app.secret import *
from flask_sqlalchemy import SQLAlchemy
from flask_autodoc.autodoc import Autodoc

import json

app = Flask(__name__)
app.config.from_object('app.configure')
autodoc = Autodoc(app)
db = SQLAlchemy(app)

white_list = ['/', '/home', '/hello', '/give_me_json', '/login', '/signup']
@app.before_request
def beforeRequest() :
	for i in white_list: 
		if str(request.url_rule) == i: return
	if '/doc' in str(request.url): return
	if current_user.is_anonymous: return jsonify({'success':0, 'msg':'please login'})

from app.Controller import init_controller
from app.Model import init_db
from app.login import init_login
from app.admin import init_admin

init_db()
init_controller(app)
init_login(app)
init_admin(app)