from model import db, datetime, Schema, fields, removeProfile, DATETIME, BASE, FIELD, STATUS, MSG, Validator
import uuid

class UserModel(db.Model):
  __tablename__ = 'users'
  username = db.Column(db.String, primary_key=True)
  fullname = db.Column(db.String(500), nullable=False)
  isAdmin =  db.Column(db.Boolean, nullable=False, default=False)
  token = db.Column(db.String(500), nullable=True)
  create_date = db.Column(db.String(20), nullable=True)
  active = db.Column(db.Boolean, nullable=False, default=False)

  def __init__(self, username, fullname, isAdmin=False, token=None, create_date=None, active=True):
    self.username = username
    self.fullname = fullname
    self.isAdmin = isAdmin
    self.token = token
    self.create_date = datetime.datetime.now().strftime(DATETIME.DATETIME_FORMAT_YYYYMMDD_HHMMSS)
    self.active = active

  def __init__(self):
    self.username = ''
    self.fullname = ''
    self.token = ''
    self.active = True

  def is_exits(self):
    return True;

  def is_authenticated(self):
    return True

  def is_active(self):
    return self.active

  def is_admin(self):
    return self.isAdmin

  def to_dict(self, many=False):
    userschema = UserSchema(many=many)
    return userschema.dump(self).data

  def from_json(data, field_mapping):
    user = UserModel()
    for idx, itm in enumerate(field_mapping):
      if itm in data:
        if type(data[itm]) is bool:
          user.__dict__[itm] = data[itm]
        elif type(data[itm]) is int:
          user.__dict__[itm] = data[itm]
        elif len(data[itm]) > 0:
          user.__dict__[itm] = data[itm]
    if len(user.token) <= 0:
      user.token = BASE.AUTO_GEN_TOKEN
    user.create_date = datetime.datetime.now().strftime(DATETIME.DATETIME_FORMAT_YYYYMMDD_HHMMSS)
    return user

  def update_object(self, model, field_mapping):
    for idx, itm in enumerate(field_mapping):
      if itm in model:
        if type(model[itm]) is bool:
          setattr(self, itm, model[itm])
        elif type(model[itm]) is int:
          setattr(self, itm, model[itm])
        elif len(model[itm]) > 0:
          setattr(self, itm, model[itm])
    if len(self.token) <= 0:
      self.token = BASE.AUTO_GEN_TOKEN
    self.create_date = datetime.datetime.now().strftime(DATETIME.DATETIME_FORMAT_YYYYMMDD_HHMMSS)
    return self

class UserSchema(Schema):
  username = fields.Str()
  fullname = fields.Str()
  isAdmin = fields.Boolean()
  token = fields.Str()
  create_date = fields.Str()
  active = fields.Boolean()