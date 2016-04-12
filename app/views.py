from app import app
from flask import request
from werkzeug import secure_filename
from flask_wtf import Form
from flask_wtf.file import FileField, FileAllowed, FileRequired

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


class icalForm(Form):
    icalFile = FileField('Your ical', validators=[
        FileRequired(),
        FileAllowed(['ics'], '.ics files only')
    ])


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    form = icalForm()
    if form.validate_on_submit():
        filename = secure_filename(form.icalFile.data.filename)
        form.icalFile.data.save('uploads/' + filename)
    else:
        filename = None
    return render_template('upload.html', form=form, filename=filename)