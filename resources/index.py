from flask_restful import Resource

class Home(Resource):
  def index():
    return jsonify({})
  def Login():
    return