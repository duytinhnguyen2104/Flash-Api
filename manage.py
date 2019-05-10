# import system
import os
import uuid
# import unittest
import coverage
import unittest

# import manage comandline
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# import server
from server.server import app, datetime

from model.UserModel import UserModel, db

from core.constant import DateTimeFormart as DATETIME

COV = coverage.coverage(
    branch=True,
    # Các file cần test
    include='./*',
    # loại bỏ những file không cần test
    omit=['*/tests/*', 'manage.py']
)
COV.start()

migrate = Migrate(app, db)

manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def test():
    """Runs the unit tests without coverage."""
    tests = unittest.TestLoader().discover(start_dir='tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    else:
        return 1

@manager.command
def cov():
    """Runs the unit tests with coverage."""
    tests = unittest.TestLoader().discover(start_dir='tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    COV.stop()
    COV.save()
    print('Coverage Summary:')
    COV.report()
    basedir = os.path.abspath(os.path.dirname(__file__))
    covdir = os.path.join(basedir, 'reports/coverage')
    COV.html_report(directory=covdir)
    print('HTML version: file://%s/index.html' % covdir)
    COV.erase()

@manager.command
def migrate():
    db.create_all()

@manager.command
def drop_db():
    db.drop_all()

@manager.command
def create_admin():
    """Creates the admin user."""
    data = [
        {
            'username': 'thongnm',
            'fullname': 'thongnm',
            'token': str(uuid.uuid4()),
            'active': True,
            'isAdmin': True,
            'create_date': datetime.datetime.now().strftime(DATETIME.DATETIME_FORMAT_YYYYMMDD_HHMMSS)
        },
        {
            'username': 'cuongmh',
            'fullname': 'cuongmh',
            'token': str(uuid.uuid4()),
            'active': True,
            'isAdmin': False,
            'create_date': datetime.datetime.now().strftime(DATETIME.DATETIME_FORMAT_YYYYMMDD_HHMMSS)
        },
        {
            'username': 'hantt',
            'fullname': 'hantt',
            'token': str(uuid.uuid4()),
            'active': True,
            'isAdmin': False,
            'create_date': datetime.datetime.now().strftime(DATETIME.DATETIME_FORMAT_YYYYMMDD_HHMMSS)
        },
        {
            'username': 'hieutc',
            'fullname': 'hieutc',
            'token': str(uuid.uuid4()),
            'active': True,
            'isAdmin': False,
            'create_date': datetime.datetime.now().strftime(DATETIME.DATETIME_FORMAT_YYYYMMDD_HHMMSS)
        },
        {
            'username': 'hungmh',
            'fullname': 'hungmh',
            'token': str(uuid.uuid4()),
            'active': True,
            'isAdmin': False,
            'create_date': datetime.datetime.now().strftime(DATETIME.DATETIME_FORMAT_YYYYMMDD_HHMMSS)
        },
        {
            'username': 'hungnq',
            'fullname': 'hungnq',
            'token': str(uuid.uuid4()),
            'active': True,
            'isAdmin': False,
            'create_date': datetime.datetime.now().strftime(DATETIME.DATETIME_FORMAT_YYYYMMDD_HHMMSS)
        },
        {
            'username': 'linhtd',
            'fullname': 'linhtd',
            'token': str(uuid.uuid4()),
            'active': True,
            'isAdmin': False,
            'create_date': datetime.datetime.now().strftime(DATETIME.DATETIME_FORMAT_YYYYMMDD_HHMMSS)
        },
        {
            'username': 'thienlh',
            'fullname': 'thienlh',
            'token': str(uuid.uuid4()),
            'active': True,
            'isAdmin': False,
            'create_date': datetime.datetime.now().strftime(DATETIME.DATETIME_FORMAT_YYYYMMDD_HHMMSS)
        },
        {
            'username': 'trangntt',
            'fullname': 'trangntt',
            'token': str(uuid.uuid4()),
            'active': True,
            'isAdmin': False,
            'create_date': datetime.datetime.now().strftime(DATETIME.DATETIME_FORMAT_YYYYMMDD_HHMMSS)
        },
        {
            'username': 'tynv',
            'fullname': 'tynv',
            'token': str(uuid.uuid4()),
            'active': True,
            'isAdmin': False,
            'create_date': datetime.datetime.now().strftime(DATETIME.DATETIME_FORMAT_YYYYMMDD_HHMMSS)
        },
    ]
    for itm in data:
        user = UserModel()
        user.username= itm.get('username')
        user.fullname= itm.get('fullname')
        # user.isAdmin=itm.get('isAdmin'),
        user.token= itm.get('token')
        user.create_date=itm.get('create_date')
        # user.active = itm.get('active')
        db.session.add(user)
        db.session.commit()

if __name__ == '__main__':
    manager.run()