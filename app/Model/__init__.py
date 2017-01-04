from app import db

def init_db() :
	## Add Models
	import app.Model.UserModel as userModel

	db.create_all()

	print 'Database initialized'
