import os


baseDir = os.path.abspath(os.path.dirname(__file__))



class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or '123456'

	# url的格式为：数据库的协议： // 用户名：密码 @ ip地址：端口号（默认可以不写） / 数据库名
	#                 mysql ://   root : QAZwsx123. @ localhost/app
	SQLALCHEMY_DATABASE_URI = "mysql://root:QAZwsx123.@localhost/app"
	SQLALCHEMY_TRACK_MODIFICATIONS = False



