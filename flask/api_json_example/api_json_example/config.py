class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = 'temporary_secret_key'

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    CSRF_ENABLED = False

