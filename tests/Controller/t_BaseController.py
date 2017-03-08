import pytest
from json import dumps, loads
from app import app as Application, db as ApplicationDatabase
@pytest.fixture(scope='module')
def app() :
	return Application.test_client()
@pytest.fixture(scope='module')
def db() :
	return ApplicationDatabase

def test_root(app, db) :
	data = app.get('/').data
	assert data == 'home'
def test_home(app, db) :
	data = app.get('/hello').data
	assert data == 'Hello'
def test_give_me_json(app, db) :
	data = app.get('/give_me_json').data
	assert loads(data) == dict(success=1)