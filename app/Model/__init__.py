# -*- coding: utf-8 -*-

from app import db

def init_db() :
	## Add Models
	import app.Model.UserModel as userModel
	import app.Model.StudyModel as studyModel
	import app.Model.EventModel as eventModel
	import app.Model.PlaceModel as placeModel
	import app.Model.FoodModel as foodModel

	db.create_all()

	print 'Database initialized'
