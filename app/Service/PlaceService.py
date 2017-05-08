
from app.Model.PlaceModel import Place
from app import db
from datetime import datetime, timedelta

def put(obj, **kwargs) :
    for key in kwargs.keys() :
        if hasattr(obj, key) : setattr(obj, key, kwargs[key])

def get(id):
	return db.session.query(Place).get(id)

def getAll():
	return db.session.query(Place).all()

def create(**args):
	obj = Place(**args)
	db.session.add(obj)
	db.session.commit()
	return obj

def delete(obj):
	db.session.delete(obj) 
	db.session.commit()