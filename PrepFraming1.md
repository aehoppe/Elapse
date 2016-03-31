**Preparation / Framing
Technical Review 1
Gaby Clarke and Alex Hoppe**

# Background and Context
**Project Goal**
We are making a calendar visualization tool with a sleek user interface to empower people to understand how they manage their time.

**Implementation**
We are using the icalendar python library to parse .ics text files, which essentially just puts all the attributes into a dictionary-like object.  We are currently planning to use pyd3 for data visualization, which is a python interface for d3js.  We have also found the vincent library, which uses vega.  We are open to suggestions for better python data visualization libraries.

**Stretch Goal**
- web app
- compiled calendar of Olin public events
- host on RPi

# Agenda
1. Project overview
2. Data parsing and management
3. Data visualization

# Questions
- What information would be cool to have in a data visualization?
- How should we store our data?  Should we pickle it? (Because we can pickle that…)
- How should we address privacy concerns surround people’s personal data?
- What python library would be best for us to use for data visualization?
- How should we visualize time?