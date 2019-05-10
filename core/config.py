import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False

    SECRET_KEY = 'ngminhthong.cntp@gmail.com'

    DB_USER = 'root'

    DB_PASS = ''

    DB_HOST = 'localhost'

    DB_PORT = '3306'

    DB_NAME = 'Flask_face_recognition'

    DB_LOCAL = './database'

    DB_PROVIDER = 'sqlite:///'

    DB_URL = DB_PROVIDER + DB_LOCAL + DB_NAME



class DevelopmentConfig(Config):
    """
        Configurations for Development.
    """
    DEBUG = True


class TestingConfig(Config):
    
    """
        Configurations for Testing
    """
    TESTING = True
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = True

    DB_PROVIDER = 'sqlite:///'

    DB_LOCAL = 'database'

    DB_NAME = 'Flask_face_recognition.db'

    DB_URL = DB_PROVIDER + os.path.join(DB_LOCAL, DB_NAME)

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'product': ProductionConfig
}