from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.Model import db

## import Models
from app.Model.UserModel import User
##

from flask_login import current_user

class AdminOnlyModelView(ModelView) :
	def is_accessible(self) :
		return current_user.is_authenticated and current_user.role == 'ADMIN'
	def inaccessible_callback(self, name, **kwargs) :
		return jsonify({'success':0, 'msg': 'admin only'})

def init_admin(app) :
	admin = Admin(app, name='pysocc', template_mode='bootstrap3')

	## add Model
	## ex : admin.add_view(AdminOnlyModelView(<Model>, db.session))
	##
	admin.add_view(AdminOnlyModelView(User, db.session))

	print 'Admin init'