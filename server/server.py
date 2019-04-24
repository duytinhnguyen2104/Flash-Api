from flask import Blueprint
from flask_restful import Api
from flask_static_compress import FlaskStaticCompress
from core.config import app_config

class server():
  def __init__():
    app = Blueprint('face_recognition', __name__,  'static')
    FlaskStaticCompress(app)
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    api = Api(app)