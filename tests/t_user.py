import pytest
from json import dumps, loads
from app import app as Application, db as ApplicationDatabase
from app.Model.UserModel import User
@pytest.fixture(scope='module')
def app() :
	return Application.test_client()
@pytest.fixture(scope='module')
def db() :
	return ApplicationDatabase

import random

def baseLogin(app, db) :
	email = ''.join(randomChar() for i in range(10)) + '@gmail.com'
	password = ''.join(randomChar() for i in range(10))
	ep = dumps(dict(email=email, password=password))
	res = app.post('/signup', data=ep)
	dataJson = loads(res.data)
	assert dataJson['success'] == 1

	user = db.session.query(User).filter(User.email == email).first()
	assert user

	res = app.post('/login', data=ep)
	dataJson = loads(res.data)
	assert dataJson['success'] == 1
	return email, password, ep

def baseLoginEnd(app, db) :
	res = app.post('/signout')
	dataJson = loads(res.data)
	if dataJson['success'] == 0 : print dataJson['msg']
	assert dataJson['success'] == 1

def randomChar() :
	return chr(random.randint(ord('a'),ord('z')))

def test_signup_login_logout_signout(app, db) :
	email, password, ep = baseLogin(app, db)

	res = app.post('/logout')
	dataJson = loads(res.data)
	assert dataJson['success'] == 1

	app.post('/login',data=ep)
	baseLoginEnd(app, db)