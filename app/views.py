""" Elapse
    SoftDes Final Project

    author: Gaby Clarke, Alex Hoppe
"""

from app import app
from flask import request, render_template
from werkzeug import secure_filename
from flask_wtf import Form
from flask_wtf.file import FileField, FileAllowed, FileRequired

# INDEX APP ROUTES
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


class icalForm(Form):
    """ ical file upload form """
    icalFile = FileField('Your ical', validators=[
        FileRequired(),
        FileAllowed(['ics'], '.ics files only')
    ])


# ICAL UPLOAD PAGE
@app.route('/upload', methods=['POST', 'GET'])
def upload():
    form = icalForm()
    if form.validate_on_submit():
        filename = secure_filename(form.icalFile.data.filename)
        form.icalFile.data.save('uploads/' + filename)
    else:
        filename = None
    return render_template('upload.html', form=form, filename=filename)


# VIS1 VIEW PAGE
@app.route('/vis1')
def vis1():
    return render_template('templates/vis1.html')

# edit calendar event tags
@app.route('/edit')
def edit():
    return render_template('templates/edit.html', events=cal.events)
