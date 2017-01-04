
def init_controller(app) :
	from app.Controller.BaseController import baseCnt
	from app.Controller.UserController import userCnt

	app.register_blueprint(baseCnt)
	app.register_blueprint(userCnt)

	print 'controller init'