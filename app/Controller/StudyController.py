# -*- coding: utf-8 -*-

from flask import Blueprint, request, session, jsonify, render_template
from flask_login import login_required, current_user
from app.Misc.my_getter import data_get

import app.Service.UserService as userService
import app.Service.StudyService as studyService

from app import autodoc as auto

studyCnt = Blueprint('studyCnt', __name__)

@studyCnt.route('/study', methods=['POST'])
@auto.doc('study')
def postStudy() :
    try :
        success, bodyJson = data_get()
        if studyService.checkName(bodyJson['name']) : raise Exception()
        study = studyService.create(owner_id=current_user.id, **bodyJson)
        if not study : raise Exception()
        return jsonify({'success':1, 'study':study.dict()})
    except Exception as e :
        return jsonify({'success':0, 'msg':'failed to create study'})

@studyCnt.route('/study/<int:id>', methods=['GET'])
@auto.doc('study')
def getStudy(id) :
    try :
        study = studyService.get(id)
        if not study: raise Exception()
        return jsonify({'success':1, 'study':study.dict(join=True)})
    except Exception as e:
        print e
        return jsonify({'success':0, 'msg':'failed to get study by id: {}'.format(id)})
@studyCnt.route('/study/page/<int:page>', methods=['GET'])
def getStudyPage(page) :
    try :
        studies = studyService.getPage(page=page, **request.args)
        return jsonify({'success':1, 'studies': [i.dict() for i in studies]})
    except Exception as e:
        print e
        return jsonify({'success':0, 'msg': str(e)})
@studyCnt.route('/study/<int:id>', methods=['PUT'])
@auto.doc('study')
def putStudy(id) :
    try :
        study = studyService.get(id)
        if not study: raise Exception('failed to find study by id: {}'.format(id))
        success, bodyJson = data_get()
        for key in bodyJson.keys() :
            if hasattr(study,key) : setattr(study,key,bodyJson[key])
        return jsonify({'success':1})
    except Exception as e:
        print e
        return jsonify({'success':0}) 

@studyCnt.route('/study/<int:id>', methods=['DELETE'])
@auto.doc('study')
def deleteStudy(id) :
    try :
        study = studyService.get(id)
        if not study: raise Exception()
        if current_user.id != study.owner_id : raise Exception()
        studyService.delete(study)
        return jsonify({'success':1, 'msg':'successfully deleted study {}'.format(id)})
    except Exception as e:
        print e
        return jsonify({'success':0, 'msg':'failed to delete study {}'.format(id)})

########################################################################################################
# Study Issue
########################################################################################################

@studyCnt.route('/study/<int:id>/issues', methods=['GET'])
@auto.doc('study')
def getStudyIssues(id) :
    try :
        study = studyService.get(id)
        if not study: raise Exception()
        return jsonify({'success':1, 'issues':[i.dict() for i in study.issues]})
    except Exception as e:
        print e
        return jsonify({'success':0})

@studyCnt.route('/study/<int:studyId>/issue', methods=['POST'])
@auto.doc('study')
def postStudyIssue(studyId) :
    try :
        success, bodyJson = data_get()
        issue = studyService.createIssue(study_id=studyId, **bodyJson)
        if not issue : raise Exception()
        return jsonify({'success':1, 'issue':issue.dict()})
    except Exception as e :
        print e
        return jsonify({'success':0})

@studyCnt.route('/study/issue/<int:id>', methods=['GET'])
@auto.doc('study')
def getStudyIssue(id) :
    try :
        issue = studyService.getIssue(id)
        if not issue : raise Exception()
        return jsonify({'success':1, 'issue':issue.dict()})
    except Exception as e:
        print e
        return jsonify({'success':0})

@studyCnt.route('/study/issue/<int:id>', methods=['PUT'])
@auto.doc('study')
def putStudyIssue(id) :
    try :
        issue = studyService.getIssue(id)
        if not issue: raise Exception()
        success, bodyJson = data_get()
        for key in bodyJson.keys() :
            if hasattr(issue, key) : setattr(issue, key, bodyJson[key])
        return jsonify({'success':1})
    except Exception as e:
        print e
        return jsonify({'success':0})

@studyCnt.route('/study/issue/<int:id>', methods=['DELETE'])
@auto.doc('study')
def deleteStudyIssue(id) :
    try :
        issue = studyService.getIssue(id)
        if not issue : raise Exception()
        studyService.delete(issue)
        return jsonify({'success':1})
    except Exception as e :
        print e
        return jsonify({'success':0})