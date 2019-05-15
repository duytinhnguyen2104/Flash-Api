from model import db, Schema, fields, DATETIME, STATUS, MSG, Validator, FIELD, BASE, datetime

class TrainingModel(db.Model):
  __tablename__ = 'trains'
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  # value face
  X = db.Column(db.String,  nullable=True)
  # Value key user
  Y= db.Column(db.String,  nullable=True)

  create_date = db.Column(db.String(20), nullable=True)

  create_user = db.Column(db.String, nullable=True)

  list_user = db.Column(db.String, nullable=True)

  def __init__(self):
    self.X = ''
    self.Y = ''
    self.create_user = ''
    self.create_date = datetime.datetime.now().strftime(DATETIME.DATETIME_FORMAT_YYYYMMDD_HHMMSS)
    self.list_user = ''

  def to_dict(self, many=False):
    training = TrainingSchema(many=many)
    return training.dump(self).data

  def from_json(data, field_mapping):
    train = TrainingModel()
    for idx, itm in enumerate(field_mapping):
      if itm in data:
        if len(data[itm]) > 0:
          train.__dict__[itm] = data[itm]
    if 'username' in data and len(data['username']) > 0:
      train.create_user = data['username']
    train.list_user = '_'.join(set(data['Y'].split('_')))
    train.create_date = datetime.datetime.now().strftime(DATETIME.DATETIME_FORMAT_YYYYMMDD_HHMMSS)
    return train


class TrainingSchema(Schema):
  X = fields.Str()
  Y = fields.Str()