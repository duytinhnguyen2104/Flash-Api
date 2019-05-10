from flask import Flask, Blueprint, make_response, abort, jsonify, render_template, request
from flask_static_compress import FlaskStaticCompress
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_claims
import jwt, os, jinja2
import argparse, re
import datetime

#=============================import from project===========================
from core.config import app_config
from core.logger import logger
from core.response import handle_error
from core.utils import moveFile, makeFile, training, makeError, getUser, getUserDetail, removeProfile, makeDir

app = Flask(__name__, root_path='.')

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.static_folder = 'static'
jwt = JWTManager(app)
FlaskStaticCompress(app)

