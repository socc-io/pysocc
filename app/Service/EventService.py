# -*- coding: utf-8 -*-

from app.Model.EventModel import Event, EventComment
from app import db
from datetime import datetime, timedelta

DEFAULT_PAGE_SIZE = 20


def put(obj, **kwargs) :
    for key in kwargs.keys() :
        if hasattr(obj, key) : setattr(obj, key, kwargs[key])

def get(id) :
	return db.session.query(Event).get(id)

def getAll() :
	return db.session.query(Event).all()

def getPage(page, writer_id=None, study_id=None, **kwargs) :
	q = db.session.query(Event) # make Query
	pageSize = args.get('pageSize') or DEFAULT_PAGE_SIZE
	if writer_id != None:
		q = q.filter(Event.writer_id == int(writer_id)) # add filter
	if study_id  != None:
		q = q.filter(Event.study_id == int(study_id)) # add filter
	return q.limit(pageSize).offset(pageSize*page).all() # set pager and get all

def getComment(id) :
	return db.session.query(EventComment).get(id)

def getWithRange(left, right) :
	leftDate  = datetime.strptime(left, '%Y-%m-%d') # parse to Date object
	rightDate = datetime.strptime(right,'%Y-%m-%d')
	return db.session.query(Event).filter(Event.date >= leftDate).filter(Event.date <= rightDate).all()

def create(**args) :
	obj = Event(**args)
	db.session.add(obj)
	db.session.commit()
	return obj

def createComment(**args):
	obj = EventComment(**args)
	db.session.add(obj)
	db.session.commit()
	return obj

def delete(obj) :
	db.session.delete(obj)
	db.session.commit()