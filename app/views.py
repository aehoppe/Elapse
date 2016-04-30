
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
ical = None
visChoice = 'donut'
dateRange = None


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
        week = request.form['dateRange']
        startMonday = datetime.datetime.strptime(week + '-1', "%Y-W%W-%w")
        global dateRange
        dateRange = startMonday, startMonday + datetime.timedelta(days=6)
        file = request.files['icalFile']
        if file and allowed_file(file.filename) and startMonday:
            filename = secure_filename(file.filename)
            file.save(os.path.join('app/static/uploads/cal.ics'))
            return redirect(url_for('edit'))

    return render_template('upload.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# EDIT CALENDAR EVENTS
@app.route('/edit', methods=['POST', 'GET'])
def edit():
    global ical
    ical = Calendar('cal')
    ical.parse_ical('app/static/uploads/cal.ics')
    global dateRange
    #timezone-awareness check
    tzDefault = ical.events[0].startTime.tzinfo
    dateRange = (dateRange[0].replace(tzinfo=tzDefault), dateRange[1].replace(tzinfo=tzDefault))

    newevents = []
    for event in ical.events:
        if event.startTime >= dateRange[0] and event.endTime <= dateRange[1]:
            newevents.append(event)
    ical.events = newevents

    eventStrings = []
    for e in ical.events:
        # print asciify(e.name)
        eventStrings.append(str(e.startTime.month) +'/'+ str(e.startTime.day) + ' ' + e.name)
    return render_template('edit.html', events=eventStrings)

def asciify(strn):
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
        # try:
        global ical
        global dateRange
        vis.visualize(ical, visChoice, dateRange=dateRange)
        # except:
        #     print 'didnt output vis' + str(datetime.datetime.now())
        # theFile= jsonify("vis.json")
        return redirect(url_for('visualize'))
    return render_template('choose.html')


# SHOW VISUALIZATION
@app.route('/visualize', methods=['POST', 'GET'])
def visualize():
    return render_template('visualize.html')
