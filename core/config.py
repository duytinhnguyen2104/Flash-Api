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



class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
}