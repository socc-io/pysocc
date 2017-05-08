# -*- coding: utf-8 -*-

from app import db
from datetime import datetime, timedelta

event_attendance = db.Table('event_attendance',
	db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
	db.Column('event_id', db.Integer, db.ForeignKey('event.id'))
)

class Event(db.Model):
	"""Event Model"""
	__tablename__ = 'event'
	id = db.Column(db.Integer, primary_key=True)
	writer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	study_id = db.Column(db.Integer, db.ForeignKey('study.id'))
	place_id = db.Column(db.Integer, db.ForeignKey('place.id'))
	date = db.Column(db.DateTime)
	content = db.Column(db.Text)

	writer = db.relationship('User')
	study = db.relationship('Study')
	place = db.relationship('Place')
	foods = db.relationship('Food', secondary='event_with_food')
	attending_users = db.relationship('User', secondary=event_attendance)
	def __init__(self, writer_id, date, content='', study_id=None):
		self.writer_id = writer_id
		self.date = datetime.strptime(date, '%Y-%m-%d')
		self.content = content
		self.study_id = study_id
	def __repr__(self):
		return '<Event date:{}, content: {}>'.format(self.date, self.content)
	def dict(self, join=False) :
		base = {
			'id': self.id,
			'writer_id': self.writer_id,
			'study_id': self.study_id,
			'place_id': self.place_id,
			'date': self.date,
			'content': self.content
		}
		if join:
			joined = {
				'writer': self.writer.dict(),
				'place': self.place.dict(),
				'study': self.study.dict(),
				'foods': [i.dict() for i in self.foods],
				'attending_users': [i.dict() for i in self.attending_users]
			}
			base = dict(base, **joined)
		return base

class EventComment(db.Model) :
	__tablename__ = 'eventcomment'
	id = db.Column(db.Integer, primary_key=True)
	event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
	writer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	created_date = db.Column(db.DateTime)
	content = db.Column(db.Text)

	event = db.relationship('Event')
	writer = db.relationship('User')

	def __init__(self, event_id, writer_id, content, created_date=None) :
		self.event_id = event_id
		self.writer_id = writer_id
		self.content = content
		self.created_date = created_date or datetime.now()
	def __repr__(self) :
		return '<EventComment, content: {}>'.format(self.content)
	def dict(self, join=False) :
		base = {
			'id': self.id,
			'event_id': self.event_id,
			'writer_id' : self.writer_id,
			'created_date' : self.created_date,
			'content' : self.content
		}
		if join :
			joined = {
				'event': self.event.dict(),
				'writer': self.writer.dict()
			}
			base = dict(base, **joined)
		return base