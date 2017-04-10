# -*- coding: utf-8 -*-

from app.Model.EventModel import Event
from app import db
from datetime import datetime, timedelta

DEFAULT_PAGE_SIZE = 20

def get(id) :
	return db.session.query(Event).get(id)
def getAll() :
	return db.session.query(Event).all()
def getPage(page, args) :
	q = db.session.query(Event)
	pageSize = args.get('pageSize') or DEFAULT_PAGE_SIZE
	with args.get('writer_id') as writer_id :
		if writer_id != None :
			q = q.filter(Event.writer_id == int(writer_id))
	return q.limit(pageSize).offset(pageSize*page).all()
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