from app import db
from app.Model.UserModel import User

import datetime

def findByRole(role, **kwargs) :
	userList = db.session.query(User).filter(User.role == role).all()
	return userList, 'success'

def findOneByEmail(email, **kwargs) :
	user = db.session.query(User).filter(User.email == email).first()
	if user :
		return user, 'success'
	else :
		return user, 'not found'

def signup(email, password, **kwargs) :
	check_user = db.session.query(User).filter(User.email == email).first()
	if check_user :
		return None, 'Already mail exists'
	user = User(email=email, password=password)
	db.session.add(user)
	db.session.commit()
	return user, 'success'

def updateLastDate(user, **kwargs) :
	user.last_date = datetime.datetime.now()

def delete(obj) :
	db.session.delete(obj)
	db.session.commit()
