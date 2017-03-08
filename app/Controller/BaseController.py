from flask import Blueprint, jsonify, Response, redirect
from app.secret import *

import os

baseCnt = Blueprint('baseCnt', __name__)

@baseCnt.route('/', methods=['GET'])
def getHome() :
	return 'home'
@baseCnt.route('/hello', methods=['GET'])
def sayHello() :
	return 'Hello'
@baseCnt.route('/give_me_json', methods=['GET'])
def giveMeJson() :
	return jsonify({'success':1})