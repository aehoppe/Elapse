""" Elapse
    SoftDes Final Project

    author: Gaby Clarke, Alex Hoppe
"""

from app import app
from app import ALLOWED_EXTENSIONS, UPLOAD_FOLDER
from flask import request, render_template, redirect, url_for, send_from_directory
from werkzeug import secure_filename
from flask_wtf import Form
import visualize as vis
import os

icalFile = 'test'
visChoice = 'donut'
daterange = None

#+++++++++++++++++++++++++++++
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

#+++++++++++++++++++++++++++++

# INDEX
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# ABOUT THE PROJECT
@app.route('/about')
def about():
    return render_template('about.html')

# UPLOAD ICAL
@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        # startDate = request.form['dateRangeStart']
        # endDate = request.form['dateRangeEnd']
        # print type(startDate)
        file = request.files['icalFile']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join('app/uploads/cal.ics'))
            return redirect(url_for('choose'))

    return render_template('upload.html')

    # return '''
    # <!doctype html>
    # <title>Upload new File</title>
    # <h1>Upload new File</h1>
    # <form action="" method=post enctype=multipart/form-data>
    # <p><input type=file name=file>
    # <input type=submit value=Upload>
    # </form>
    # '''

# EDIT CALENDAR EVENTS
@app.route('/edit', methods=['POST', 'GET'])
def edit():
    global icalFile
    return render_template('edit.html', events=icalFile.events)

# CHOOSE A VISUALIZATION
@app.route('/choose', methods=['POST', 'GET'])
def choose():
    if request.method == 'POST':
        global visChoice
        visChoice = request.form['visChoice']
        vis.visualize(os.path.join('app/uploads/cal.ics'), visChoice, daterange=daterange)

        return redirect(url_for('visualize'))
    return render_template('choose.html')

# SHOW VISUALIZATION
@app.route('/visualize', methods=['POST', 'GET'])
def visualize():
    return render_template('visualize.html')

@app.route('/json/<filename>')
def json(filename):
    return send_from_directory('json', filename)
