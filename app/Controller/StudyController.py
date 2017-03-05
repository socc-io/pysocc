from flask import Blueprint, request, session, jsonify, render_template
from flask_login import login_required, current_user

import app.Service.UserService as userService
import app.Service.StudyService as studyService

studyCnt = Blueprint('studyCnt', __name__)

@studyCnt.route('/study', methods=['POST'])
def postStudy() :
    try :
        bodyJson = request.get_json()
        study = studyService.create(**bodyJson)
        if not study : raise Exception()
        return jsonify({'success':1, 'study':study.dict()})
    except Exception as e :
        return jsonify({'success':0, 'msg':'failed to create study'})

@studyCnt.route('/study/<int:id>', methods=['GET'])
def getStudy(id) :
    try :
        study = studyService.get(id)
        if not study: raise Exception()
        return jsonify({'success':1, 'study':study.dict(join=True)})
    except :
        return jsonify({'success':0, 'msg':'failed to get study by id: {}'.format(id)})

@studyCnt.route('/study/<int:id>', methods=['PUT'])
def putStudy(id) :
    try :
        study = studyService.get(id)
        if not study: raise Exception('failed to find study by id: {}'.format(id))
    except :
        return jsonify({'success':0}) 

@studyCnt.route('/study/<int:id>', methods=['DELETE'])
def deleteStudy(id) :
    try :
        if studyService.delete(id) :
            return jsonify({'success':0, 'msg':'successfully deleted study {}'.format(id)})
        else : raise Exception()
    except :
        return jsonify({'success':0, 'msg':'failed to delete study {}'.format(id)})
