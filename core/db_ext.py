from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import app_config
from sqlalchemy import text, create_engine

class Db():
  def session():
    basemodel = declarative_base()
    engine = create_engine(app_config.get('product').DB_URL)
    basemodel.metadata.bind = engine
    DBSession = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    return DBSession()

  def excQuery(query):
    conn = Db.session()
    sql = text(query)
    raw_data = conn.execute(sql).fetchall()
    conn.close()
    return raw_data

  def exeNoneQuery(query):
    conn = Db.session()
    sql = text(query)
    conn.execute(sql)
    conn.commit()
    conn.close()
