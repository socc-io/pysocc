# -*- coding: utf-8 -*-

from flask import Blueprint, request, session, jsonify, render_template
from flask_login import login_required, current_user
from app.Misc.my_getter import data_get
import app.Service.FoodService as foodService
from app import autodoc as auto

foodCnt = Blueprint('foodCnt', __name__)

@foodCnt.route('/food/<int:foodId>', methods=['GET', 'PUT', 'DELETE'])
def aboutFood(foodId):
	try:
		food = foodService.get(foodId)
		if not food: raise Exception('food not found')
		if request.method == 'GET':
			return jsonify({'success':1, 'food': food.dict(True)})
		elif request.method == 'PUT':
			if current_user.role != 'ADMIN': raise Exception('no permission')
			success, bodyJson = data_get()
			foodService.put(food, **bodyJson)
			return jsonify({'success':1})
		elif request.method == 'DELETE':
			if current_user.role != 'ADMIN': raise Exception('no permission')
			foodService.delete(food) 
			return jsonify({'success':1})
	except Exception as e:
		print e
		return jsonify({'success':0, 'error': str(e)})

@foodCnt.route('/food', methods=['POST'])
def postFood():
	try:
		if current_user.role != 'ADMIN': raise Exception('no permission')
		success, bodyJson = data_get()
		food = foodService.create(**bodyJson)
		return jsonify({'success':1, 'food': food.dict()})
	except Exception as e:
		print e
		return jsonify({'success':0, 'error': str(e)})

###############################################
# FoodImage
###############################################

@foodCnt.route('/food/image/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def aboutFoodImage(id):
	try:
		image = foodService.getImage(id)
		if not image: raise Exception('image not found')
		if request.method == 'GET':
			return jsonify({'success':1, 'image': image.dict(True)})
		elif request.method == 'PUT':
			if current_user.role != 'ADMIN': raise Exception('no permission')
			success, bodyJson = data_get()
			foodService.put(image, **bodyJson)
			return jsonify({'success': 1})
		elif request.method == 'DELETE':
			if current_user.role != 'ADMIN': raise Exception('no permission')
			foodService.delete(image)
			return jsonify({'success':1})
	except Exception as e:
		print e
		return jsonify({'success':0, 'error': str(e)})

@foodCnt.route('/food/<int:foodId>/image', methods=['POST'])
def postFoodImage(foodId):
	try:
		food = foodService.get(foodId)
		if not food: raise Exception('food not found')
		
		success, bodyJson = data_get()
		image = foodService.createImage(foodId=foodId, **bodyJson)

		return jsonify({'success':1, 'image': image.dict()})
	except Exception as e:
		print e
		return jsonify({'success':0, 'error': str(e)})