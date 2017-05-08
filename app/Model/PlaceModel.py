
from app import db
from datetime import datetime, timedelta

class Place(db.Model):
	__tablename__ = 'place'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(256))
	latitude = db.Column(db.Float)
	longitude = db.Column(db.Float)
	place_type = db.Column(db.String(64))

	foods = db.relationship('Food', secondary='place_has_food')

	def __init__(self, name=None, latitude=None, longitude=None, place_type=None):
		self.name = name
		self.latitude = latitude
		self.longitude = longitude
		self.place_type = place_type

	def __repr__(self):
		return '<Place, name: {}, place_type: {}>'.format(self.name, self.place_type)

	def dict(self, join=False):
		base = {
			'id' : self.id,
			'name' : self.name,
			'latitude' : self.latitude,
			'longitude' : self.longitude,
			'place_type' : self.place_type
		}
		if join:
			joined = {
				'foods': [i.dict() for i in self.foods]
			}
			base = dict(base, **joined)
		return base