""" Elapse
    SoftDes Final Project

    author: Gaby Clarke, Alex Hoppe
"""

from app import app
from flask import request, render_template
from werkzeug import secure_filename
from flask_wtf import Form
from visualize import visualize

icalFile = 'test'

# INDEX
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# UPLOAD ICAL
@app.route('/upload', methods=['POST', 'GET'])
def upload():
    icalFile = request.form['icalFile']
    print icalFile
    global filename
    filename = '' #just for now...
    global dateRange
    dateRange = None #just for now...
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
        visualize(filename, visChoice, dateRange)
    return render_template('choose.html')

# SHOW VISUALIZATION
@app.route('/visualize')
def visualize():
    return render_template('visualize.html')