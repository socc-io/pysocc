from test.Controller import controllerTest
from test.Model import modelTest
from test.Service import serviceTest
from app import app, db

def test(app, db) :
	controllerTest(app, db)
	modelTest(app, db)
	serviceTest(app, db)