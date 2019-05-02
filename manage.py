import os
import coverage
import unittest
from flask_script import Manager
from flask import Flask

COV = coverage.coverage(
    branch=True,
    include='.',
    omit=[
        'test/*'
    ]
)
COV.start()

app = Flask(__name__)

manager = Manager(app)

@manager.command
def cov():
  """Runs the unit tests with coverage."""
  tests = unittest.TestLoader().discover('tests')
  result = unittest.TextTestRunner(verbosity=2).run(tests)
  print(result.wasSuccessful())
  COV.stop()
  COV.save()
  print('Coverage Summary:')
  COV.report()
  basedir = os.path.abspath(os.path.dirname(__file__))
  covdir = os.path.join(basedir, 'coverage')
  COV.html_report(directory=covdir)
  COV.erase()

if __name__ == '__main__':
    manager.run()