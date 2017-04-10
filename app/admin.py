# -*- coding: utf-8 -*-

from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask import render_template, jsonify
from app.Model import db

## import Models
from app.Model.UserModel import User
from app.Model.StudyModel import Study, StudyIssue
from app.Model.EventModel import Event, EventComment
##

from flask_login import current_user

class AdminOnlyModelView(ModelView) :
	def is_accessible(self) :
		return current_user.role == 'ADMIN'
	def inaccessible_callback(self, name, **kwargs) :
		return jsonify({'success':0, 'msg': 'admin only'})
class LoginView(BaseView) :
	@expose('/')
	def index(self) :
		return render_template('adminLogin.html', user=current_user)

def init_admin(app) :
	admin = Admin(app, name='pysocc', template_mode='bootstrap3')
	admin.add_view(LoginView(name='Login', menu_icon_type='glyph', menu_icon_value='glyphicon-home'))
	## add Model
	## ex : admin.add_view(AdminOnlyModelView(<Model>, db.session))
	##
	AOMV = AdminOnlyModelView
	admin.add_view(AOMV(User, db.session))
	admin.add_view(AOMV(Study, db.session))
	admin.add_view(AOMV(StudyIssue, db.session))
	admin.add_view(AOMV(Event, db.session))
	admin.add_view(AOMV(EventComment, db.session))
	print 'Admin init'