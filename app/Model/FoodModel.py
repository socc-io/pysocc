
from app import db 
from datetime import datetime, timedelta

place_has_food = db.Table('place_has_food',
	db.Column('place_id', db.Integer, db.ForeignKey('place.id')),
	db.Column('food_id', db.Integer, db.ForeignKey('food.id'))
)

event_with_food = db.Table('event_with_food',
	db.Column('event_id', db.Integer, db.ForeignKey('event.id')),
	db.Column('food_id', db.Integer, db.ForeignKey('food.id'))
)

class Food(db.Model):
	__tablename__ = 'food'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64))

	events = db.relationship('Event', secondary=event_with_food)
	places = db.relationship('Place', secondary=place_has_food)
	images = db.relationship('FoodImage')

	def __init__(self, name=None):
		self.name = name

	def __repr__(self):
		return '<Food, name: {}>'.format(self.name)

	def dict(self, join=False):
		base = {
			'id': self.id,
			'name': self.name
		}
		if join:
			joined = {
				'events': [i.dict() for i in self.events],
				'places': [i.dict() for i in self.places],
				'images': [i.dict() for i in self.images]
			}
			base = dict(base, **joined)
		return base

class FoodImage(db.Model):
	__tablename__ = 'foodimage'
	id = db.Column(db.Integer, primary_key=True)
	food_id = db.Column(db.Integer, db.ForeignKey('food.id'))
	path = db.Column(db.String(512))

	food = db.relationship('Food')

	def __init__(self, food_id, path):
		self.food_id = food_id
		self.path = path

	def __repr__(self):
		return '<FoodImage, food_id: {}>'.format(self.food_id)

	def dict(self, join=False):
		base = {
			'id': self.id,
			'food_id': self.food_id,
			'path': self.path
		}
		if join:
			joined = {
				'food': self.food.dict()
			}
			base = dict(base, **joined)
		return base
