import jwt
import random, datetime

class token():
  @staticmethod
  def auth_token(userid, app):
    try:
      payload = {
          'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=30),
          'iat': datetime.datetime.utcnow(),
          'sub': userid
      }
      return jwt.encode(
        payload,
        app.config.get('SECRET_KEY'),
        algorithm='HS256'
      ).decode()
    except Exception as e:
      return e

  @staticmethod
  def decode_auth_token(auth_token, app):
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
      payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
      return payload['sub']
    except jwt.ExpiredSignatureError:
      return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
      return 'Invalid token. Please log in again.'
