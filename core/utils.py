import os
import shutil
import re
import datetime
import base64
from PIL import Image, ImageDraw, ExifTags
from io import BytesIO

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
        if(ext.upper() == '.JPG'):
          obj = {}
          obj['url'] = url
          obj['name'] = file
          obj['user'] = username
          obj['data'] = convertImg(url)
          res.insert(count, obj)
          count = count + 1
  return res

def convertImg(url):
    image_file = Image.open(url)
    mode='RGB'
    for orientation in ExifTags.TAGS.keys():
        if ExifTags.TAGS[orientation] == 'Orientation':
            break

    if image_file._getexif() != None:
      exif = dict(image_file._getexif().items())
      if orientation in exif:
          if exif[orientation] == 3:
              image_file = image_file.rotate(180, expand=True)
          elif exif[orientation] == 6:
              image_file = image_file.rotate(270, expand=True)
          elif exif[orientation] == 8:
              image_file = image_file.rotate(90, expand=True)
    image_file = image_file.convert(mode)
    buffered = BytesIO()
    image_file.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())
    return img_str.decode("utf-8")

def removeProfile(objdata = {}, isall = False):
  if not objdata:
    return False
  try:
    if(isall):
      dst = os.path.join(TRAIN_PATH, SUB_IMG)
      dst = os.path.join(dst, objdata.get('user'))
      if(checkIsExit(dst)):
        shutil.rmtree(dst)
        return True
    elif(os.path.isfile(objdata.get('url'))):
      os.unlink(objdata.get('url'))
      return True
    return True
  except Exception as e:
    return False

def beforeRemove(url, dicttmp):
  return False

def afterRemove(url):
  return True

def cleanup_sync():
  try:
    _local = getUser()
    raw = DATABASE.excQuery('select * from users')
    user = []
    for idx, itm in enumerate(raw):
      user.insert(idx, '{0}'.format(itm['username']))

    matchlst = set(_local) & set(user)

    exist = "'" + "','".join(matchlst) + "'"

    # xoa khoi database cac user khong ton tai folder img
    sql = 'delete from users where username not in ({0})'.format(exist)

    DATABASE.exeNoneQuery(sql)
    # nén folder for backup
    file_name  = 'train_' + datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
    src = os.path.join(TRAIN_PATH, SUB_IMG)
    zipfile(file_name, src)
    # xóa thư muc
    new_list = set(_local).difference(user)
    for idx, itm in enumerate(new_list):
      data = {}
      data['user'] = itm
      removeProfile(data, isall=True)
  except Exception as e:
    return False

def zipfile(file_name, src):
  shutil.make_archive(file_name,'zip', src)
