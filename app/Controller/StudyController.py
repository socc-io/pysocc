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
    except Exception as e:
        print e
        return jsonify({'success':0, 'msg':'failed to get study by id: {}'.format(id)})

@studyCnt.route('/study/<int:id>', methods=['PUT'])
def putStudy(id) :
    try :
        study = studyService.get(id)
        if not study: raise Exception('failed to find study by id: {}'.format(id))
        bodyJson = request.get_json()
        for key in bodyJson.keys() :
            if hasattr(study,key) : setattr(study,key,bodyJson[key])
        return jsonify({'success':1})
    except Exception as e:
        print e
        return jsonify({'success':0}) 

@studyCnt.route('/study/<int:id>', methods=['DELETE'])
def deleteStudy(id) :
    try :
        study = studyService.get(id)
        if not study: raise Exception()
        studyService.delete(study)
        return jsonify({'success':1, 'msg':'successfully deleted study {}'.format(id)})
    except Exception as e:
        print e
        return jsonify({'success':0, 'msg':'failed to delete study {}'.format(id)})

########################################################################################################
# Study Issue
########################################################################################################

@studyCnt.route('/study/<int:id>/issues', methods=['GET'])
def getStudyIssues(id) :
    try :
        study = studyService.get(id)
        if not study: raise Exception()
        return jsonify({'success':1, 'issues':[i.dict() for i in study.issues]})
    except Exception as e:
        print e
        return jsonify({'success':0})

@studyCnt.route('/study/<int:studyId>/issue', methods=['POST'])
def postStudyIssue(studyId) :
    try :
        bodyJson = request.get_json()
        issue = studyService.createIssue(study_id=studyId, **bodyJson)
        if not issue : raise Exception()
        return jsonify({'success':1, 'issue':issue.dict()})
    except Exception as e :
        print e
        return jsonify({'success':0})

@studyCnt.route('/study/issue/<int:id>', methods=['GET'])
def getStudyIssue(id) :
    try :
        issue = studyService.getIssue(id)
        if not issue : raise Exception()
        return jsonify({'success':1, 'issue':issue.dict()})
    except Exception as e:
        print e
        return jsonify({'success':0})

@studyCnt.route('/study/issue/<int:id>', methods=['PUT'])
def putStudyIssue(id) :
    try :
        issue = studyService.getIssue(id)
        if not issue: raise Exception()
        bodyJson = request.get_json()
        for key in bodyJson.keys() :
            if hasattr(issue, key) : setattr(issue, key, bodyJson[key])
        return jsonify({'success':1})
    except Exception as e:
        print e
        return jsonify({'success':0})

@studyCnt.route('/study/issue/<int:id>', methods=['DELETE'])
def deleteStudyIssue(id) :
    try :
        issue = studyService.getIssue(id)
        if not issue : raise Exception()
        studyService.delete(issue)
        return jsonify({'success':1})
    except Exception as e :
        print e
        return jsonify({'success':0})