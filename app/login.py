from flask_login import LoginManager
from app.Model.UserModel import User
from app.Model import db

login_manager = LoginManager()

login_manager.login_view  = 'users.login'

@login_manager.user_loader
def load_user(email) :
	return db.session.query(User).filter(User.email == email).first()

@login_manager.request_loader
def load_user_from_request(request) :
	api_key = request.args.get('api_key')
	if api_key :
		user = db.session.query(User).filter(User.apikey == api_key).first()
		if user :
			return user
	api_key = request.headers.get('authorization')
	if api_key :
		user = db.session.query(User).filter(User.apikey == api_key).first()
		if user :
			return user
	return None

def init_login(app) :
	login_manager.init_app(app)
	print 'Login initialized'