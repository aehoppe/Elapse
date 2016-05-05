
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
    """ The main page for the project """
    return render_template('index.html')


# ABOUT THE PROJECT
@app.route('/about')
def about():
    """ Links from the main page to our documentation landing page """
    return render_template('about.html')
@app.route('/implementation')
def implementation():
    """ Implementation page"""
    return render_template('implementation.html')


# UPLOAD ICAL
@app.route('/upload', methods=['POST', 'GET'])
def upload():
    """ Handles uploaded files and date range selection and directs to chooose
     if a post request, renders the upload form otherwise """
    if request.method == 'POST':
        week = request.form['dateRange']
        startMonday = datetime.datetime.strptime(week + '-1', "%Y-W%W-%w")
        global dateRange
        dateRange = startMonday, startMonday + datetime.timedelta(days=6)
        file = request.files['icalFile']
        if file and allowedFile(file.filename) and startMonday:
            filename = secure_filename(file.filename)
            file.save(os.path.join('app/static/uploads/cal.ics'))
            return redirect(url_for('edit'))

    # Otherwise just show the upload page
    return render_template('upload.html')

def allowedFile(filename):
    """ Filename checking for uploads using Werkzeug, don't want anyone touching
    internal files or uploading things they're not allowed to """
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# EDIT CALENDAR EVENTS
@app.route('/edit', methods=['POST', 'GET'])
def edit():
    """ Right now just parses specifically the events in the calendar in the
    date range selected on the upload page. Also checks for timezone compliance.
    Shows the events in the range for user verification.
    """
    #Send along once they approve the events
    if request.method == 'POST':
        return redirect(url_for('choose'))

#### PARSING CALENDAR
    global ical
    ical = Calendar('cal')
    ical.parseical('app/static/uploads/cal.ics')
    global dateRange
    #timezone-awareness check
    tzDefault = ical.events[0].startTime.tzinfo
    dateRange = (dateRange[0].replace(tzinfo=tzDefault), dateRange[1].replace(tzinfo=tzDefault))

    # only get the events that are in our date range.
    newevents = []
    for event in ical.events:
        if type(event.startTime) != datetime.date:
            if event.startTime >= dateRange[0] and event.endTime <= dateRange[1]:
                newevents.append(event)
    ical.events = newevents

    # Get the names of the events for debugging or plotting in the future
    eventStrings = []
    for e in ical.events:
        # print asciify(e.name)
        eventStrings.append(str(e.startTime.month) +'/'+ str(e.startTime.day) + ' ' + e.name)
    return render_template('edit.html', events=eventStrings)

def asciify(strn):
    """ Turns unicode into ascii. Not particularly helpful, but at least Flask
    can handle it.
    """
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
    """ Renders a form for the user to pick a visualization style, also handles
    the request and displays the visualization """
    if request.method == 'POST':
        global visChoice
        visChoice = request.form['visChoice']
        print visChoice
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
    """ Displays the visualization by rendering the JSON object that represents
    the viz in the app/static/json """
    return render_template('visualize.html')
