from flask import Blueprint, request, session, jsonify, render_template
from flask_login import login_required, current_user

import app.Service.EventService as eventService

eventCnt = Blueprint('eventCnt', __name__)

@eventCnt.route('/event', methods=['POST'])
def postEvent() :
	try :
		if current_user.is_anonymous : raise Exception()
		bodyJson = request.get_json()
		event = eventService.create(writer_id=current_user.id,**bodyJson)
		if not event: raise Exception()
		return jsonify({'success':1, 'event':event.dict()})
	except Exception as e :
		print e
		return jsonify({'success':0})
@eventCnt.route('/event/<int:id>', methods=['GET'])
def getEvent(id) :
	try :
		event = eventService.get(id)
		if not event: raise Exception()
		return jsonify({'success':1, 'event':event.dict(True)})
	except Exception as e:
		print e
		return jsonify({'success':0})
@eventCnt.route('/event/range/<string:left>/<string:right>', methods=['GET'])
def getEventWithRange(left, right) :
	try :
		events = eventService.getWithRange(left, right)
		if not events: raise Exception()
		return jsonify({'success':1, 'events':[i.dict() for i in events]})
	except Exception as e :
		print e
		return jsonify({'success':0})
@eventCnt.route('/event/<int:id>', methods=['PUT'])
def putEvent(id) :
	try :
		event = eventService.get(id)
		if not event: raise Exception()
		bodyJson = request.get_json()
		for key in bodyJson.keys() :
			if hasattr(event, key): setattr(event, key, bodyJson[key])
		return jsonify({'success':1})
	except Exception as e:
		print e
		return jsonify({'success':0})
@eventCnt.route('/event/<int:id>', methods=['DELETE'])
def deleteEvent(id) :
	try :
		event = eventService.get(id)
		if not event: raise Exception()
		eventService.delete(event)
		return jsonify({'success':1})
	except Exception as e:
		print e
		return jsonify({'success':0})