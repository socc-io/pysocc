from flask import Blueprint, request, session, jsonify, render_template
from flask_login import login_user, logout_user, login_required, current_user

from app.Model.UserModel import User

from app.Misc.my_getter import data_get

import app.Service.UserService as userService
import app.Service.StudyService as studyService

from app import autodoc as auto

import hashlib

userCnt = Blueprint('userCnt', __name__)

@userCnt.route('/whoami', methods=['GET'])
@auto.doc('user')
def whoami() :
    if current_user.is_anonymous :
        return jsonify({'success':0, 'msg':'you are not logined'})
    else:
        return jsonify({'success':1, 'user':current_user.dict()})

@userCnt.route('/login', methods=['GET', 'POST'])
@auto.doc('user')
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
        m = hashlib.sha256(); m.update(data.get('password').strip());
        if user.password != m.hexdigest() :
            return jsonify({'success':0, 'msg':'invalid password'})
        login_user(user)
        userService.updateLastDate(user)
        return jsonify({'success':1, 'user':user.dict()})

@userCnt.route('/logout', methods=['POST'])
@auto.doc('user')
def logout() :
    if not current_user.is_anonymous :
        logout_user()
    return jsonify({'success':1})

@userCnt.route('/signup', methods=['POST'])
@auto.doc('user')
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

@userCnt.route('/signout', methods=['POST'])
@auto.doc('user')
def signout() :
    try :
        if current_user.is_anonymous : raise Exception()
        userService.delete(current_user)
        return jsonify({'success':1})
    except Exception as e :
        print e
        return jsonify({'success':0})

@userCnt.route('/join_study/<int:studyNo>', methods=['POST'])
@auto.doc('user')
def postJoinStudy(studyNo) :
    if current_user.is_anonymous :
        return jsonify({'success':0, 'msg':'login required'})
    study = studyService.get(studyNo)
    if not study:
        return jsonify({'success':0, 'msg':'failed to find study {}'.format(studyNo)})
    current_user.studies.append(study)
    return jsonify({'success':1})

@userCnt.route('/exit_study/<int:studyNo>', methods=['POST'])
@auto.doc('user')
def postExitStudy(studyNo) :
    if current_user.is_anonymous :
        return jsonify({'success':0, 'msg':'login required'})
    study = studyService.get(studyNo)
    if not study:
        return jsonify({'success':0, 'msg':'failed to find study {}'.format(studyNo)})
    current_user.studies.remove(study)
    return jsonify({'success':1})