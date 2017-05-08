# -*- coding: utf-8 -*-

from flask import Blueprint, request, session, jsonify, render_template
from flask_login import login_required, current_user
from app.Misc.my_getter import data_get
import app.Service.PlaceService as placeService
from app import autodoc as auto

placeCnt = Blueprint('placeCnt', __name__)

@placeCnt.route('/place/<int:placeId>', methods=['GET', 'PUT', 'DELETE'])
def aboutPlace(placeId):
	try:
		place = placeService.get(placeId)
		if not place: raise Exception('place not found')
		if request.method == 'GET':
			return jsonify({'success':1, 'place': place.dict(True)})
		elif request.method == 'PUT':
			if current_user.role != 'ADMIN': raise Exception('no permission')
			success, bodyJson = data_get()
			placeService.put(place, **bodyJson)
			return jsonify({'success':1})
		elif request.method == 'DELETE':
			if current_user.role != 'ADMIN': raise Exception('no permission')
			placeService.delete(place) 
			return jsonify({'success':1})
	except Exception as e:
		print e
		return jsonify({'success':0, 'error': str(e)})

@placeCnt.route('/place', methods=['POST'])
def postPlace():
	try:
		if current_user.role != 'ADMIN': raise Exception('no permission')
		success, bodyJson = data_get()
		place = placeService.create(**bodyJson)
		return jsonify({'success':1, 'place': place.dict()})
	except Exception as e:
		print e
		return jsonify({'success':0, 'error': str(e)})