from app import db

def init_db() :
	## Add Models
	import app.Model.UserModel as userModel
        import app.Model.StudyModel as studyModel

	db.create_all()

	print 'Database initialized'
