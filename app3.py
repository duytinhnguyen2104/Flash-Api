from flask import Flask, jsonify, request, json, render_template, url_for, abort, make_response
from flask_static_compress import FlaskStaticCompress
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_claims
import jwt
import re, datetime

# from core.utils import makeDir, deleteTmpFolder, moveFile, makeFile, training, makeError
# from core.logger import logger
# from core.response import handle_error
# from core.config import app_config
# from core.token import token

app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = 'ngminhthong.cntp@gmail.com'
app.static_folder = 'static'
compress = FlaskStaticCompress(app)

jwt = JWTManager(app)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

@app.errorhandler(405)
def not_found(error):
    return make_response(jsonify( { 'error': 'Method Not Allowed' } ), 405)

@app.errorhandler(500)
def not_found(error):
    return make_response(jsonify( { 'error': 'Internal Server Error' } ), 500)

@app.route('/')
def index():
  return render_template('index.html')

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

@jwt.user_claims_loader
def add_claims_to_access_token(identity):
    return {
        'authen': identity
    }

@app.route('/Signin', methods=['POST'])
def signin():
  username = request.json.get('username', None)
  ret = {'access_token': create_access_token(identity=username,expires_delta=datetime.timedelta(days=0, seconds=3600))}
  return jsonify(ret), 200

@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    claims = get_jwt_claims()
    return jsonify({
        'userId': claims['authen']
    }), 200


if __name__ == '__main__':
    app.run(host='192.168.10.114', port=9000, debug=True)
