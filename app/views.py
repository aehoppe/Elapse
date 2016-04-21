""" Elapse
    SoftDes Final Project

    author: Gaby Clarke, Alex Hoppe
"""

from app import app
from flask import request, render_template
from werkzeug import secure_filename
from flask_wtf import Form

icalFile = 'test'

# INDEX
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# UPLOAD ICAL
@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        print icalFile
    return render_template('upload.html')

# EDIT CALENDAR EVENTS
@app.route('/edit', methods=['POST', 'GET'])
def edit():
    global icalFile
    print icalFile
    return render_template('edit.html', events=icalFile.events)

# CHOOSE A VISUALIZATION
@app.route('/choose', methods=['POST', 'GET'])
def choose():
    if request.method == 'POST':
        global visChoice
        visChoice = request.form['visChoice']
        print visChoice
        if visChoice == 'stackedArea':
            pass
        if visChoice == 'donut':
            pass
    return render_template('choose.html')

# SHOW VISUALIZATION
@app.route('/visualize')
def visualize():
    return render_template('visualize.html')
