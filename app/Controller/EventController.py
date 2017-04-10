# -*- coding: utf-8 -*-

from flask import Blueprint, request, session, jsonify, render_template
from flask_login import login_required, current_user
from app.Misc.my_getter import data_get
import app.Service.EventService as eventService
from app import autodoc as auto

eventCnt = Blueprint('eventCnt', __name__)

@eventCnt.route('/event', methods=['POST'])
@auto.doc('event')
def postEvent() :
	try :
		success, bodyJson = data_get()
		event = eventService.create(writer_id=current_user.id,**bodyJson)
		if not event: raise Exception()
		return jsonify({'success':1, 'event':event.dict()})
	except Exception as e :
		print e
		return jsonify({'success':0})
@eventCnt.route('/event/<int:id>', methods=['GET'])
@auto.doc('event')
def getEvent(id) :
	try :
		event = eventService.get(id)
		if not event: raise Exception()
		return jsonify({'success':1, 'event':event.dict(True)})
	except Exception as e:
		print e
		return jsonify({'success':0})
@eventCnt.route('/event/page/<int:page>', methods=['GET'])
def getEventPage(page) :
	try :
		events = eventService.getPage(page=page, **request.args)
		return jsonify({'success':1, 'events': [i.dict() for i in events]})
	except Exception as e:
		print e
		return jsonify({'success':0})
@eventCnt.route('/event/range/<string:left>/<string:right>', methods=['GET'])
@auto.doc('event')
def getEventWithRange(left, right) :
	try :
		events = eventService.getWithRange(left, right)
		if not events: raise Exception()
		return jsonify({'success':1, 'events':[i.dict() for i in events]})
	except Exception as e :
		print e
		return jsonify({'success':0})
@eventCnt.route('/event/<int:id>', methods=['PUT'])
@auto.doc('event')
def putEvent(id) :
	try :
		event = eventService.get(id)
		if not event: raise Exception()
		bodyJson = data_get()
		for key in bodyJson.keys() :
			if hasattr(event, key): setattr(event, key, bodyJson[key])
		return jsonify({'success':1})
	except Exception as e:
		print e
		return jsonify({'success':0})
@eventCnt.route('/event/<int:id>', methods=['DELETE'])
@auto.doc('event')
def deleteEvent(id) :
	try :
		event = eventService.get(id)
		if not event: raise Exception(u'존재하지 않는 이벤트입니다')
		if current_user.id != event.writer_id: raise Exception(u'작성자만 지울 수 있습니다')
		eventService.delete(event)
		return jsonify({'success':1})
	except Exception as e:
		print e
		return jsonify({'success':0, 'msg':str(e)})

########################################################################################################
# Event Comment
########################################################################################################

@eventCnt.route('/event/<int:event_id>/comment', methods=['POST'])
def postEventComment(event_id) :
	try :
		success, bodyJson = data_get()
		comment = eventService.createComment(event_id=event_id, **bodyJson)
		if not comment: raise Exception()
		return jsonify({'success':1, 'comment':comment.dict()})
	except Exception as e :
		print e
		return jsonify({'success':0})