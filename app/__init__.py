from flask import Flask

import os
app = Flask(__name__)
app.config.from_object('config')

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['ics'])

from app import views
