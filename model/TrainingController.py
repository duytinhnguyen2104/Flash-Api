from controller.TrainingModel import TrainingModel, db, DATETIME, STATUS, MSG, Validator, FIELD, BASE
from core.db_ext import Db as DB_EXT
class TrainingController(TrainingModel):
  
  def getList():
    max_id = db.session.query(db.func.max(TrainingModel.id)).scalar()
    train = db.session.query(TrainingModel).filter(TrainingModel.id == max_id).all()
    if train and len(train) == 1:
      meta = meta = TrainingModel.to_dict(train[0])
      return {'status': True, 'statuscode': STATUS.COD200, 'message': MSG.SUCCESS, 'train': meta}
    else:
      return {'status': False, 'statuscode': STATUS.COD404, 'message': MSG.NOT_FOUND }

  def register(model):
    if not model:
      return {'status': False, 'statuscode': STATUS.COD400, 'message': MSG.BAD_REQUEST}
    valid = []
    for idx, itm in enumerate(Validator.TABLE_TRAIN):
      if itm not in model:
        valid.insert(idx, itm)
      elif len(model[itm]) <= 0:
        valid.insert(idx, itm)
    if len(valid) > 0 :
      return {'status': False, 'statuscode': STATUS.COD400, 'message': MSG.BAD_REQUEST}
    train = TrainingModel.from_json(model, FIELD.TABLE_TRAIN)
    db.session.add(train)
    db.session.commit()
    meta = TrainingModel.to_dict(train)
    return {'status': True, 'statuscode': STATUS.COD201, 'message': MSG.SUCCESS, 'user': meta}

  def remove(userId):
    if not userId:
      return {'status': False, 'user':{}, 'statuscode': STATUS.COD500, 'message': MSG.BAD_REQUEST}
    train = TrainingModel.query.filter_by(Y=userId).all()
    if not train:
      return {'status': False, 'user':{}, 'statuscode': STATUS.COD404, 'message': MSG.NOT_EXIST.format(userId)}
    delete_q = TrainingModel.__table__.delete().where(TrainingModel.Y == userId)
    db.session.execute(delete_q)
    db.session.commit()
    return {'status': True, 'statuscode': STATUS.COD204, 'message': MSG.NO_CONTENT}

  def multiRegister(arr_X, arr_Y, username=None):
    Y = '_'.join(str(x) for x in arr_Y)
    X = '_'.join(str(' '.join(str(x) for x in v)) for v in arr_X)
    data = {}
    data['Y'] = Y
    data['X'] = X
    data['username'] = username
    return TrainingController.register(data)

  def _list(query=None):
    sql = ''
    if not query:
      sql = 'select MAX(id), X, Y from trains'
    else:
      sql = query
    raw = DB_EXT.excQuery(sql)
    if raw:
      model = TrainingModel()
      model.X = str(raw[0]['X'])
      model.Y = str(raw[0]['Y'])
      meta = TrainingModel.to_dict(model)
      return {'status': True, 'statuscode': STATUS.COD200, 'message': MSG.SUCCESS, 'train': meta}
    else:
      return {'status': False, 'statuscode': STATUS.COD404, 'message': MSG.NOT_FOUND }

  def insert(arr_x, arr_y):
    try:
      X = '_'.join(str(' '.join(str(x) for x in v)) for v in arr_x)
      Y = '_'.join(str(x) for x in arr_y)
      sql = 'INSERT INTO trains (X, Y) VALUES(%s, %s'.format(X, Y)
      DB_EXT.exeNoneQuery(sql)
      return {'status': True, 'statuscode': STATUS.COD201, 'message': MSG.SUCCESS}
    except Exception as e:
      return {'status': False, 'statuscode': STATUS.COD500, 'message': MSG.FAILS }