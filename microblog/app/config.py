import os


baseDir = os.path.abspath(os.path.dirname(__file__))



class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or '123456'

	SQLALCHEMY_DARABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(baseDir, 'app.db')

	SQLALcHEMY_TRACE_MODIFICATIONS = False



