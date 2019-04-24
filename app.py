from flask import (
  Flask, jsonify, request, json, render_template, url_for
)
from flask_static_compress import FlaskStaticCompress
from flask_jwt_extended import (
  JWTManager, jwt_required, create_access_token, get_jwt_claims
)

from core.utils import (
  makeDir, deleteTmpFolder, moveFile, makeFile, training, makeError
)

import re
from core.logger import logger
from core.response import handle_error
from core.config import app_config

from core.token import token

app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = 'ngminhthong.cntp@gmail.com'
app.static_folder = 'static'
compress = FlaskStaticCompress(app)

JWTManager(app)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/Login', methods=['POST'])
def login():
  return jsonify({'status': 'success'})

@app.route('/addUserImage', methods=['POST'])
def addUserImage():
  try:
    data = request.get_json()
    imgstr = re.search(r'base64,(.*)', str(data.get('image_data'))).group(1)   
    makeFile(imgstr, data.get('username'), data.get('index'))
    flag = False
    if data.get('index') == 10:
      moveFile()
      training()
      flag = True
    message = 'Upload succes'
    if flag:
      message = 'Upload and Training success'
    result = {"index": data.get('index'), "status": True, "message": message}
    return jsonify(result)
  except Exception as e:
    logger.insertLog('Exception:', makeError(e))
    return handle_error(e)

@app.route('/createToken', methods=['POST'])
def createToken():
  try:
    value = token.auth_token('Thongnm', app)
    return jsonify({'token': str(value)})
  except Exception as e:
    logger.insertLog('Exception:', makeError(e))
    return handle_error(e)

@app.route('/decodeToken', methods=['POST'])
def decodeToken():
  try:
    val = request.get_json().get('token')
    value = token.decode_auth_token(val, app)
    return jsonify({'token': str(value)})
  except Exception as e:
    logger.insertLog('Exception:', makeError(e))
    return handle_error(e)

@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    claims = get_jwt_claims()
    return jsonify({
        'hello_is': claims['hello'],
        'foo_is': claims['foo']
    }), 200


if __name__ == '__main__':
    app.run(debug=True)
