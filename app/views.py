""" Elapse
    SoftDes Final Project

    author: Gaby Clarke, Alex Hoppe
"""

from app import app
from app import ALLOWED_EXTENSIONS, UPLOAD_FOLDER
from flask import request, render_template, redirect, url_for
from werkzeug import secure_filename
from flask_wtf import Form
import visualize as vis
import os

icalFile = 'test'
visChoice = 'donut'

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

# UPLOAD ICAL
@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join('app/uploads/cal.ics'))
            return redirect(url_for('choose'))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
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
        vis.visualize(os.path.join('app/uploads/cal.ics'), visChoice)
        return redirect(url_for('visualize'))
    return render_template('choose.html')

# SHOW VISUALIZATION
@app.route('/visualize', methods=['POST', 'GET'])
def visualize():
    return render_template('visualize.html')
