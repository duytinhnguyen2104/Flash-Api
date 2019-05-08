from server import (
  # base
  app, render_template, request, re, #, args
  abort, make_response, jsonify, 
  # utils
  logger, handle_error,
  makeError, moveFile, training, makeFile, getUser, getUserDetail, removeProfile
)

import uuid
# ================================== start handle error ==================================
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

# ================================== start render ==================================
@app.route('/home_page/<username>')
def home_page(username):
    data = {'username': username}
    return render_template("home_page.html", data=data)

@app.route('/', methods=['POST'])
def login_using_face():
  # data = {"time": args["time_waiting"], "duration": args["duration_waiting"], "count_fail": args["count_fail_valid"]}
  data = {}
  # return render_template("login_using_face.html", data=data)
  return jsonify({"data": request.get_json()}), 200

@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")

@app.route('/login_test')
def login_test():
    return render_template("login_test.html")

@app.route('/login_using_user_pass')
def login_using_user_pass():
    return render_template("login_using_user_pass.html")

@app.route('/add_user_image')
def add_user_image():
    return render_template("add_user_image.html")

# ================================== LINK API ==================================
@app.route('/face_recognition_func/', methods=['POST'])
def face_recognition_func():
    try:
        # return obj_face_recognition.face_recognition_func()
        return jsonify({"status": "Login success"})
    except Exception as e:
        logger.insertLog('Exception:', makeError(e))
        return handle_error(e)

@app.route('/addUserImage', methods=['POST'])
def addUserImage():
    try:
        if not request.json:
          abort(400)
        data = request.get_json()
        imgstr = data.get('image_data') # re.search(r'base64,(.*)', str(data.get('image_data'))).group(1)   
        makeFile(imgstr, data.get('username'), data.get('index'))
        flag = False
        if data.get('index') == 10:
            moveFile()
            training(data.get('username'))

            flag = True
        
        message = 'Upload succes'
        
        if flag:
            message = 'Upload and Training success'
        
        result = {"index": data.get('index'), "status": True, "message": message}
        return jsonify(result)
    except Exception as e:
        logger.insertLog('Exception:', makeError(e))
        return handle_error(e)
# ================================== LINK API ==================================

@app.route('/userlist', methods=['GET'])
def userlist():
  try:
    users = getUser()
    return render_template('user_list.html', data=users)
  except Exception as e:
    logger.insertLog('Exception:', makeError(e))
    return handle_error(e)

@app.route('/userdetail/<username>', methods=['GET'])
def userdetail(username):
  try:
    detail = getUserDetail(username)
    # return jsonify(detail)
    return render_template('user_detail.html', detail = detail, user=username)
  except Exception as e:
    logger.insertLog('Exception:', makeError(e))
    return handle_error(e)

@app.route('/removeProfile/<isall>', methods=['POST'])
def remove(isall):
  try:
    if not request.get_json():
      abort(400)
    data = request.get_json()
    active = True if isall == 'true' else False
    isresult = removeProfile(data, isall=active)
    message = "Success" if isresult else "Fails"
    result = {"status": isresult, "message": message, 'router': 'userdetail'}
    return jsonify(result)
  except Exception as e:
    logger.insertLog('Exception', makeError(e))
    return handle_error(e)