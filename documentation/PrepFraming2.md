**Preparation / Framing
Technical Review 2
Gaby Clarke and Alex Hoppe**

# Background and Context
**Project Goal**
We are making a calendar visualization tool with a sleek user interface to empower people to understand how they manage their time.

**Implementation**
We have built a web app in Flask (which will eventually be a Heroku app).  In the app, the user uploads a calendar file (.ics), selects a date range to visualize, edits the calendar data as necessary, and chooses a visualization.  We are using the icalendar library to parse .ics text files, which essentially just puts all the attributes into a dictionary-like object, and the vincent library to visualize the data.  Vincent creates JSON objects, which we then render in an HTML template statically.

**Stretch Goal**
- dynamic web app implementation
- compiled calendar of Olin public events
- host on RPi

# Agenda
1. Overview
2. Status update
3. Editing data in-app
4. Data management

# Questions
- What interface should we have for tagging events?
    - Should we have color tagging?
- Should we have default categories to choose from?
- Should the uploaded data be stored so that it can be accessed later?
    - Should we implement a login system?