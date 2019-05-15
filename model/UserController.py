from model.UserModel import UserModel, db, datetime, removeProfile, DATETIME, STATUS, MSG, Validator, FIELD, BASE
import uuid

class UserController(UserModel):
  def login(userId):
    if not userId:
      return {'status': False, 'user':{}, 'statuscode': STATUS.COD500}
    user = UserModel.query.filter_by(username=userId).first()
    if user:
      meta = UserModel.to_dict(user)
      return {'status': True, 'statuscode': STATUS.COD200,  'message': MSG.SUCCESS, 'user': meta}
    else:
      return {'status': False, 'statuscode': STATUS.COD404,  'message': MSG.MSG.NOT_EXIST.format(userId)}

  def register(model):
    if not model:
      return {'status': False, 'statuscode': STATUS.COD400, 'message': MSG.BAD_REQUEST}
    valid = []
    for idx, itm in enumerate(Validator.TABLE_USER):
      if itm not in model:
        valid.insert(idx, itm)
      elif len(model[itm]) <= 0:
        valid.insert(idx, itm)
    if len(valid) > 0 :
      return {'status': False, 'statuscode': STATUS.COD400, 'message': MSG.BAD_REQUEST}
    user_check = UserModel.query.filter_by(username=model.get('username')).first()
    if user_check:
      return {'status': False, 'statuscode': STATUS.COD403, 'message': MSG.EXIST_DATA.format(model.get('username'))}
    user = UserModel.from_json(model, FIELD.TABLE_USER)
    db.session.add(user)
    db.session.commit()
    meta = meta = UserModel.to_dict(user)
    return {'status': True, 'statuscode': STATUS.COD201, 'message': MSG.SUCCESS, 'user': meta}

  def getList():
    users = UserModel.query.order_by(UserModel.username).all()
    if users:
      meta = meta = UserModel.to_dict(users, many=True)
      return {'status': True, 'statuscode': STATUS.COD200, 'message': MSG.SUCCESS, 'users': meta}
    else:
      return {'status': False, 'statuscode': STATUS.COD404, 'message': MSG.NOT_FOUND }

  def remove(userId):
    if not userId:
      return {'status': False, 'user':{}, 'statuscode': STATUS.COD500, 'message': MSG.BAD_REQUEST}
    user = UserModel.query.get(userId)
    if not user:
      return {'status': False, 'user':{}, 'statuscode': STATUS.COD404, 'message': MSG.NOT_EXIST.format(userId)}
    data = {}
    data['user'] = userId
    success = removeProfile(data, isall=True)
    if success:
      db.session.delete(user)
      db.session.commit()
      return {'status': True, 'statuscode': STATUS.COD204, 'message': MSG.NO_CONTENT}
    else:
      return {'status': False, 'statuscode': STATUS.COD400, 'message': MSG.FAILS}

  def update(model, userId):
    if not userId:
      return {'status': False, 'user':{}, 'statuscode': STATUS.COD500, 'message': MSG.BAD_REQUEST}
    user = UserModel.query.get(userId)
    if not user:
      return {'status': False, 'user':{}, 'statuscode': STATUS.COD404, 'message': MSG.NOT_EXIST.format(userId)}
    valid = []
    for idx, itm in enumerate(Validator.TABLE_USER_UPD):
      if itm not in model:
        valid.insert(idx, itm)
      elif len(model[itm]) <= 0:
        valid.insert(idx, itm)
    if len(valid) > 0 :
      return {'status': False, 'statuscode': STATUS.COD400, 'message': MSG.BAD_REQUEST}
    UserModel.update_object(user, model, FIELD.TABLE_USER_UPD)    
    db.session.commit()    
    meta = meta = UserModel.to_dict(user)    
    return {'status': True, 'statuscode': STATUS.COD200, 'message': MSG.SUCCESS, 'user': meta}