import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	DEBUG = False
	TESTING = False
	CSRF_ENABLED = True
	SECRET_KEY = 'notasecret'


class DevelopmentConfig(Config):
	DEVELOPMENT = True
	DEBUG = True


class HerokuConfig(Config):
	DEBUG = False