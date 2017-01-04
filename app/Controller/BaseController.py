from flask import Blueprint, jsonify, Response, redirect
from app.secret import *

import os

baseCnt = Blueprint('baseCnt', __name__)

@baseCnt.route('/')
def getHome() :
	return 'Hello'
