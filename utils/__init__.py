from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import app_config

basemodel = declarative_base()

def create_connect():
  engine = create_engine(app_config.get('product').DB_URL)
  basemodel.metadata.bind = engine
  DBSession = sessionmaker(bind=engine)
  return DBSession()