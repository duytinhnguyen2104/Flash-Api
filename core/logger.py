import logging
import datetime
from .utils import makeDir

# remote_addr
class logger():

  @staticmethod
  def insertLog(tilte='', message=''):
    makeDir(subpath='log')
    filename = 'log_%s' %(datetime.datetime.now().strftime("%Y%m%d"))
    template = './log/%s.log' %(filename)
    if not tilte:
      tilte = ''
    time = datetime.datetime.now().strftime("%Y%m%d %H:%M:%S %f")
    strTitle = 'Datetime: %s\n%s\n%s' %(time, tilte, message)
    logger = logging.getLogger()
    if not (logger.hasHandlers()):
      handle = logging.FileHandler(template, 'a', 'utf8')
      if not (handle):
        file_handler = logging.FileHandler(template, 'w', 'utf8')
        logger.addHandler(file_handler)
      else:
        logger.addHandler(handle)
    logger.setLevel(logging.INFO)
    logger.info(strTitle)
