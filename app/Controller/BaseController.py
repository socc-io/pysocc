# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, Response, redirect
from app.secret import *
from app import autodoc as auto

import os

baseCnt = Blueprint('baseCnt', __name__)

@baseCnt.route('/', methods=['GET'])
@auto.doc('base')
def getHome() :
	return 'home'
@baseCnt.route('/hello', methods=['GET'])
@auto.doc('base')
def sayHello() :
	return 'Hello'
@baseCnt.route('/give_me_json', methods=['GET'])
@auto.doc('base')
def giveMeJson() :
	return jsonify({'success':1})
@baseCnt.route('/doc')
def routeDocumentations() :
	return auto.html()