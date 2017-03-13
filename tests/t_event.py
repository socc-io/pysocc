import pytest
from json import dumps, loads
from app import app as Application, db as ApplicationDatabase
@pytest.fixture(scope='module')
def app() :
	return Application.test_client()
@pytest.fixture(scope='module')
def db() :
	return ApplicationDatabase

from tests.t_user import baseLogin, baseLoginEnd
import random
from app.Model.EventModel import Event

def test_event(app, db) :
	email, password, ep = baseLogin(app, db)
	randomContent = ''.join([chr(random.randint(ord('a'),ord('z'))) for i in range(100)])
	res = app.post('/event', data=dumps(dict(content=randomContent, date='2017-01-01')))
	dataJson = loads(res.data)
	assert dataJson['success'] == 1
	eventId = dataJson.get('event').get('id')
	assert eventId
	event = db.session.query(Event).get(eventId)
	assert event

	res = app.delete('/event/{}'.format(eventId))
	dataJson = loads(res.data)
	assert dataJson['success'] == 1
	baseLoginEnd(app, db)