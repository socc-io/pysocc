# -*- coding: utf-8 -*-

from app import db
from app.Misc import random_generate_alphabet

import datetime, hashlib

class User(db.Model) :
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True)
	apikey = db.Column(db.String(64))
	email = db.Column(db.String(256))
	password = db.Column(db.String(65))
	role = db.Column(db.String(32))
	active = db.Column(db.Integer)

	last_date = db.Column(db.DateTime)
	created_date = db.Column(db.DateTime)

	attending_events = db.relationship('Event', secondary='event_attendance')

	@property
	def is_authenticated(self) :
		return True

	@property
	def is_active(self) :
		return self.active == 1

	@property
	def is_anonymous(self) :
		return False

	def get_id(self) :
		return self.email

	def __init__(self, email, password) :
		self.email = email
		m = hashlib.sha256()
		m.update(password.strip())
		self.password = m.hexdigest()

		self.role = 'USER'
		self.active = 1
		self.apikey = random_generate_alphabet(64)

		self.created_date = datetime.datetime.now()
		self.last_date    = datetime.datetime.now()

	def dict(self) :
		return {
			'id'    : self.id,
			'apikey': self.apikey,
			'email' : self.email,
			'role'  : self.role,
			'active': self.active,
			'last_date' : self.last_date,
			'created_date' : self.created_date
		}
