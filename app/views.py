""" Elapse
    SoftDes Final Project

    author: Gaby Clarke, Alex Hoppe
"""

from app import app
from flask import request, render_template
from werkzeug import secure_filename
from flask_wtf import Form
# from flask_wtf.file import FileField, FileAllowed, FileRequired

icalFile = 'test'

# INDEX APP ROUTES
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# ICAL UPLOAD PAGE
@app.route('/upload', methods=['POST','GET'])
def upload():
    icalFile = request.form['icalFile']
    print icalFile
    return render_template('upload.html')

# EDIT CALENDAR EVENTS
@app.route('/edit', methods=['POST', 'GET'])
def edit():
    global icalFile
    print icalFile
    return render_template('edit.html', events=icalFile.events)

# VIS1 VIEW PAGE
@app.route('/vis1')
def vis1():
    return render_template('vis1.html')
