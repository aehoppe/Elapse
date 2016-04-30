""" Elapse
    SoftDes Final Project

    author: Gaby Clarke, Alex Hoppe
"""

import vincent
import datetime
import os


def visualize(cal, visualization, dateRange=None):
    """ Takes a file name (could be a file object in the future) and
    parses its cal data into a Calendar with Events, and a visualization type
    argument. It also takes an optional date range tuple of datetime objects. It
    plots the cumulative time for each event in the range specified. """

    # Set default timezone
    tzDefault = cal.events[0].startTime.tzinfo

    # Take user input for dates
    if dateRange == None:
        visRange = (datetime.datetime(2016, 5, 1, tzinfo=tzDefault), datetime.datetime(2016, 5, 7, tzinfo=tzDefault))
    else:
        visRange = dateRange

    # Find the length of the vis in days
    visDelta = (visRange[1] - visRange[0])
    visLen = visDelta.days
    if visDelta.seconds > 0 or visDelta.microseconds > 0:
        visLen += 1

    # Set up list of days to process, including the day after it ends
    daysIncluded = [visRange[0] + i*datetime.timedelta(1) for i in range(visLen + 1)]

    # Make labels
    dayStrings = [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]

    # Initialize data dictionary with index values
    data = {'index': dayStrings}

    print data

    # Clean data (no date objects allowed) and accumulate total time
    for i in range(visLen):
        for event in cal.events:
            if type(event.startTime) == datetime.date or not event.startTime.tzinfo:
                pass
            else:
                event.startTime.replace(tzinfo=tzDefault)
                event.endTime.replace(tzinfo=tzDefault)
                if event.startTime >= daysIncluded[i] and event.startTime < daysIncluded[i+1]:
                    if not data.get(event.name):
                        data[event.name] = [0 for day in range(len(daysIncluded)-1)]
                    data[event.name][i] += event.duration.seconds / 60.0**2

    # Dictionary of plotting functions
    vizzes = {u'stackedArea':stacked_area, u'donut':donut}

    # Make plot
    plot = vizzes[visualization](data)

    # Generate JSON object to render in HTML template
    plot.to_json('app/static/uploads/vis.json')


def stacked_area(data):
    """ Creates a stacked area plot visualization """

    stacked = vincent.StackedArea(data, iter_idx='index')
    stacked.axis_titles(x='Index', y='Data Value')
    stacked.legend(title='Categories')
    stacked.colors(brew='Spectral')
    return stacked


def donut(data):
    """ Creates a donut plot visualization """

    # Total the time in each category and give it back as a Pandas dataframe
    data = total_time(data)
    donut = vincent.Pie(data, inner_radius=200)
    donut.colors(brew="Set3")
    donut.legend('Categories')
    return donut


def total_time(data):
    """ Totals up the time in each category in the dataframe """

    new_data = {}
    # Total up the non-index categories
    for key in data.keys():
        if not key is 'index':
            new_data[key] = sum(data[key])
    return new_data


if __name__ == '__main__':
    import sys
    # Debug test of parsing
    try:
        name = sys.argv[1]
    except IndexError:
        name = 'stacked_area'
    visualize('Gaby.ics', name)
    os.system('firefox vis.html')
