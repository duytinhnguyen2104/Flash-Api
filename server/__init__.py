from flask import Flask, Blueprint, make_response, abort, jsonify, render_template, request
from flask_static_compress import FlaskStaticCompress
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_claims
import jwt, os, jinja2
import argparse, re
#=============================import from project===========================
from core.config import app_config
from core.logger import logger
from core.response import handle_error
from core.utils import moveFile, makeFile, training, makeError

# ap = argparse.ArgumentParser()

# # thời gian chờ tối đa để nhận diện khuôn mặt (milisecond)
# ap.add_argument("-time", "--time_waiting", required=True,
# 	help="Maximum standby time for face recognition")

# # thời gian lấy hình định kì để gửi lên server xác nhận khuôn mặt (milisecond)
# ap.add_argument("-duration", "--duration_waiting", required=True,
# 	help="Time to periodically upload images to send to face confirmation server")

# # số lần sai cho phép khi phát hiện khuôn mặt sai (không tính số lần không tìm thấy khuôn mặt, hoặc tìm thấy nhiều khuôn mặt)
# ap.add_argument("-co", "--count_fail_valid", required=True,
# 	help="The number of false positives allowed when false faces are detected")

# args = vars(ap.parse_args())

app = Flask(__name__, root_path='.')

# loader = jinja2.ChoiceLoader([
#         app.jinja_loader,
#         jinja2.FileSystemLoader('./templates')
#     ])

# app.jinja_loader = loader

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.static_folder = 'static'
jwt = JWTManager(app)
FlaskStaticCompress(app)

