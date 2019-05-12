from utils import Column, Integer, String, Boolean, basemodel

class UserModel(basemodel):
  __tablename__ = 'users'
  username = Column(String, primary_key=True)
  fullname = Column(String(500), nullable=False)
  isAdmin =  Column(Boolean, nullable=False, default=False)
  token = Column(String(500), nullable=True)
  create_date = Column(String(20), nullable=True)
  active = Column(Boolean, nullable=False, default=False)