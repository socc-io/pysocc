from flask import Blueprint, request, session, jsonify, render_template
from flask_login import login_user, logout_user, login_required, current_user

from app.Model.UserModel import User

from app.Misc.my_getter import data_get

import app.Service.UserService as userService

userCnt = Blueprint('userCnt', __name__)

@userCnt.route('/whoami')
def whoami() :
	if current_user.is_anonymous :
		return jsonify({'success':0, 'msg':'you are not logined'})
	else :
		return jsonify({'success':1, 'user':current_user.dict()})

@userCnt.route('/login')
def login() :
	if request.method == 'GET' :
		return 'login page not exists'
	elif request.method == 'POST' :
		err, data = data_get(('email', 'password'))
		if err == False :
			if data == None :
				return jsonify({'success':0, 'msg':'invalid request format'})
			else :
				return jsonify({'success':0, 'msg':'{} not found'.format(data)})
		user, db_msg = userService.findOneByEmail(data.get('email'))
		if not user :
			return jsonify({'success':0, 'msg':'invalid email'})
		if user.password != data.get('password') :
			return jsonify({'success':0, 'msg':'invalid password'})
		login_user(user)
		userService.updateLastDate(user)
		return jsonify({'success':1, 'user':user.dict()})

@userCnt.route('/logout')
def logout() :
	if not current_user.is_anonymous :
		logout_user()
	return jsonify({'success':1})

@userCnt.route('/signup', methods=['POST'])
def signup() :
	err, data = data_get(('email', 'password'))
	if err == False :
			if data == None :
				return jsonify({'success':0, 'msg':'invalid request format'}) # Fail to parse request data
			else :
				return jsonify({'success':0, 'msg':'{0} not found'.format(data)}) # Couldn't find required data
	user, msg = userService.signup(**data)
	if not user :
		return jsonify({'success':0, 'msg':msg})
	return jsonify({'success':1, 'user':user.dict()})