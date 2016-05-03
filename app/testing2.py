""" Elapse
    SoftDes Final Project
    This file implements our first visualization, parsing an ics file and plots
    the cumulative time spent on each activity in a stacked area chart.
    author: Gaby Clarke, Alex Hoppe
"""

import vincent
import elapseCalendar
import datetime
import os


def vis1(filename, daterange=None):
    '''
    This function takes a file name (could be a file object in the future) and
    parses its ical data into a Calendar with Events. It also takes an optional
    date range tuple of datetime objects. It plots the cumulative time for each
    event in the range specified.
    '''
    c = elapseCalendar.Calendar('vis1cal')
    c.parseical(filename)

    # Set default timezone
    tzDefault = c.events[0].startTime.tzinfo

    # Take user input for dates
    if daterange == None:
        visRange = (datetime.datetime(2016, 5, 1, tzinfo=tzDefault), datetime.datetime(2016, 5, 7, tzinfo=tzDefault))
    else:
        visRange = daterange

    # Find the length of the vis in days
    visDelta = (visRange[1] - visRange[0])
    visLen = visDelta.days
    if visDelta.seconds > 0 or visDelta.microseconds > 0:
        visLen += 1

    # Set up list of days to process, including the day after it ends
    daysIncluded = [visRange[0] + i*datetime.timedelta(1) for i in range(visLen + 1)]

    # Make labels
    dayStrings = [str(i) for i in range(visLen)]

    # data = {'index': daysIncluded[:-1]}
    data = {'index': dayStrings}

    # Clean data (no date objects allowed) and accumulate total time
    for i in range(visLen):
        for event in c.events:
            if type(event.startTime) == datetime.date or not event.startTime.tzinfo:
                pass
            else:
                event.startTime.replace(tzinfo=tzDefault)
                event.endTime.replace(tzinfo=tzDefault)
                if event.startTime >= daysIncluded[i] and event.startTime < daysIncluded[i+1]:
                    if not data.get(event.name):
                        data[event.name] = [0 for day in range(len(daysIncluded)-1)]
                    data[event.name][i] += event.duration.seconds / 60.0**2

    # Make plot

    data = totalTime(data)
    busyTime = sum(data.values())
    unbusyTime = 7*24 - busyTime # 7 days * 24 hours/day
    print busyTime
    business = {'unbusy':unbusyTime, 'busy':busyTime}
    busy = vincent.Pie(business)
    busy.colors(brew='BW')
    busy.legend(title="business")
    busy.to_json('vis1.json', html_out=True, html_path='vis1.html')

    # os.system('firefox vis1.html')

def totalTime(data):
    """ Totals up the time in each category in the dataframe """

    new_data = {}
    # Total up the non-index categories
    for key in data.keys():
        if not key is 'index':
            new_data[key] = sum(data[key])
    return new_data


if __name__ == '__main__':
    # Debug test of parsing
    vis1('softdes.ics')