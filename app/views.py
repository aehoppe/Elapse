
""" Elapse
    SoftDes Final Project

    This file handles all of the routing for our Flask web app. Each @app.route
    tag corresponds to a page of our website. The user interaction flow is:
        index
        |
        upload: Upload .ics files and choose date range
        |
        edit: Edit data and add tags
        |
        choose: Choose visualization
        |
        visualize: See how you use your time

    author: Gaby Clarke, Alex Hoppe
"""

from app import app
from app import ALLOWED_EXTENSIONS, UPLOAD_FOLDER
from flask import request, render_template, redirect, url_for, send_from_directory, json
from werkzeug import secure_filename
from flask_wtf import Form
import visualize as vis
import datetime
import os
from elapseCalendar import Calendar

# GLOBAL VARIABLES
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
            file.save(os.path.join('app/static/uploads/cal.ics'))
            return redirect(url_for('edit'))

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
    icalFile = Calendar('cal')
    icalFile.parse_ical('app/uploads/cal.ics')
    eventStrings = []
    for e in icalFile.events:
        print e.name
        # eventStrings.append(e.name.encode('ascii', errors='backslashreplace'))
    # print
    return render_template('edit.html', events=eventStrings)

def ascii(strn):
    output = ''
    for char in strn:
        if ord(char) < 128:
            output += str(ord(char))
        else:
            output += char
    return output


# CHOOSE A VISUALIZATION
@app.route('/choose', methods=['POST', 'GET'])
def choose():
    if request.method == 'POST':
        global visChoice
        visChoice = request.form['visChoice']
        try:
            global icalFile
            vis.visualize(icalFile, visChoice, daterange=daterange)
        except:
            print 'didnt output vis' + str(datetime.datetime.now())
        # theFile= jsonify("vis.json")
        return redirect(url_for('visualize'))
    return render_template('choose.html')

# SHOW VISUALIZATION
@app.route('/visualize', methods=['POST', 'GET'])
def visualize():
    return render_template('visualize.html')

# @app.route('/vis', methods=['POST', 'GET'])
# def vis():
#     return render_template('vis.html')

@app.route('/json/<filename>')
def json(filename):
    print filename
    return send_from_directory(filename)
