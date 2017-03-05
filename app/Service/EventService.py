from app.Model.EventModel import Event
from app import db
from datetime import datetime, timedelta

def get(id) :
	return db.session.query(Event).get(id)
def getWithRange(left, right) :
	leftDate  = datetime.strptime(left, '%Y-%m-%d')
	rightDate = datetime.strptime(right,'%Y-%m-%d')
	return db.session.query(Event).filter(Event.date >= leftDate).filter(Event.date <= rightDate).all()
def create(**args) :
	obj = Event(**args)
	db.session.add(obj)
	db.session.commit()
	return obj
def delete(obj) :
	db.session.delete(obj)
	db.session.commit()