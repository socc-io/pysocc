
def init_controller(app) :
	from app.Controller.BaseController  import baseCnt
	from app.Controller.UserController  import userCnt
	from app.Controller.StudyController import studyCnt

	app.register_blueprint(baseCnt)
	app.register_blueprint(userCnt)
	app.register_blueprint(studyCnt)

	print 'controller init'