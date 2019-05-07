import os
import shutil
import re
import datetime
import base64
from PIL import Image, ImageDraw

TEMP_PATH = 'tmp'
FULL_PATH = ''
TRAIN_PATH = 'alx_examples'
SUB_IMG = 'train'
FILE_EXTENTION = '.txt'

def checkIsExit(_path):
  return os.path.isdir(_path)

def makeDir(root=0, subpath=''):
  """
    Make folder
    Parameters:
      root: folder root: (1. TEMP_PATH, 2. TRAIN_PATH, other: Subpath)
      subpath: sub folder
    Returns: none
  """
  if root == 1:
    if not checkIsExit(TEMP_PATH):
      os.makedirs(TEMP_PATH)
    FULL_PATH = os.path.join(TEMP_PATH, subpath)
  elif root == 2:
    if not checkIsExit(TRAIN_PATH):
      os.makedirs(TRAIN_PATH)
    subtrain = os.path.join(TRAIN_PATH, SUB_IMG)
    if not checkIsExit(subtrain):
      os.makedirs(subtrain)
    FULL_PATH = os.path.join(subtrain, subpath)
  else:
    FULL_PATH = subpath
  if not checkIsExit(FULL_PATH):
    os.makedirs(FULL_PATH)
  return FULL_PATH

def deleteTmpFolder():
  """
    Descriptions: Delete all subfolder from parameter
    Parameters:
      none
  """
  for itm in os.listdir(TEMP_PATH):
    path_str = os.path.join(TEMP_PATH, itm)
    try:
      if os.path.isfile(path_str):
        os.unlink(path_str)
      elif os.path.isdir(path_str):
        shutil.rmtree(path_str)
    except Exception as e:
      print(e)

def moveFile(source='', dst=''):
  if not source:
    source = TEMP_PATH
  if not dst:
    dst = os.path.join(TRAIN_PATH, SUB_IMG)
  if checkIsExit(TEMP_PATH):
    for itm in os.listdir(TEMP_PATH):
      src = os.path.join(TEMP_PATH, itm)
      if checkIsExit(os.path.join(dst, itm)):
        copyFile(src, os.path.join(dst, itm))
      else:
        makeDir(2, itm)
        copyFile(src, os.path.join(dst, itm))
  # Delete Folder after copy to dst
  deleteTmpFolder()

def copyFile(folder, dst):
  for file in os.listdir(folder):
    src = os.path.join(folder, file)
    if(os.path.isfile(src)):
      shutil.copy(src, dst)

def makeFile(data='', UserId='', idx=0):
  """
    Description:
    Parameters:

  """
  postfix = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
  filename = UserId + '_' + str(idx) + FILE_EXTENTION  # + '_' + postfix
  prefix = makeDir(1, UserId);
  file_path = os.path.join(prefix, filename)
  with open(file_path, 'wb') as file:
    file.write(base64.b64decode(data))

def training(UserId=''):
  print("traing success")

def makeError(error):
  message = [str(x) for x in error.args]
  return message

def getUser():
  res = []
  dst = os.path.join(TRAIN_PATH, SUB_IMG)
  if(checkIsExit(dst)):
    count = 0
    for itm in os.listdir(dst):
      res.insert(count, itm)
      count = count + 1
  return res

def getUserDetail(username):
  res = []
  dst = os.path.join(TRAIN_PATH, SUB_IMG)
  dst = os.path.join(dst, username)
  if(checkIsExit(dst)):
    count = 0
    for file in os.listdir(dst):
      url = os.path.join(dst, file)
      if(os.path.isfile(url)):
        name, ext = os.path.splitext(file);
        print(ext.upper())
        if(ext.upper() == '.JPG'):
          obj = {}
          obj["url"] = url
          obj["name"] = file
          obj["user"] = username
          res.insert(count, obj)
          count = count + 1
  return res

def removeProfile(objdata = {}, isall = False):
  if not objdata:
    return False
  if(isall):
    dst = os.path.join(TRAIN_PATH, objdata.get('user'))
    if(checkIsExit(dst)):
      for itm in os.listdir(dst):
        file = os.path.join(dts)
        os.unlink(file)
        return True
  elif(os.path.isfile(objdata.get('url'))):
      # os.unlink(objdata.get('url')))
      return True
  return False