from server import app, app_config, datetime, makeDir, removeProfile

from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields
# start config database
storage = app_config.get('product').DB_LOCAL

makeDir(subpath=storage)

app.config['SQLALCHEMY_DATABASE_URI'] = app_config.get('product').DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# end config database