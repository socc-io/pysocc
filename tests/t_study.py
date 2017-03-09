import pytest
from json import dumps, loads
from app import app as Application, db as ApplicationDatabase
@pytest.fixture(scope='module')
def app() :
	return Application.test_client()
@pytest.fixture(scope='module')
def db() :
	return ApplicationDatabase
@pytest.fixture(scope='module')
def originApp() :
	return Application

def test_study(app, db, originApp) :
	##### MAKE 10 USERS
	userDatas = (dumps(dict(email='tester{}@gmail.com'.format(i), password='1234')) for i in range(1,10))
	userClients = [[originApp.test_client(), user] for user in userDatas]
	for client, data in userClients :
		client.post('/signup', data=data)
		client.post('/login',  data=data)
	##### MAKE STUDY of USER_0(king)
	king = userClients[0][0]
	res = king.post('/study', data=dumps(dict(name='StudyOfKing', description='Very Fun')))
	resJson = loads(res.data)
	assert resJson['success'] == 1
	##### JOIN STUDY
	studyId = resJson['study']['id']
	for client, data in userClients :
		client.post('/join_study/{}'.format(studyId))
	##### EXIT STUDY
	for client, data in userClients[:5] :
		client.post('/exit_study/{}'.format(studyId))
	##### DELETE STUDY
	res = king.delete('/study/{}'.format(studyId))
	assert loads(res.data)['success'] == 1
	##### DELETE 10 USERS
	for client, data in userClients :
		client.post('/signout')