import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils imports secure_filename

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER;
