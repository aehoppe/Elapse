""" Elapse
    SoftDes Final Project

    author: Gaby Clarke, Alex Hoppe
"""

import vincent
import datetime
import os


def visualize(cal, visualization, dateRange=None):
    """ Takes an elapseCalendar object, a visualization choice, and a date range.  
        Generates a vincent visualization with the given information.

        cal: elapseCalendar object
        visualization: visualization name
        dateRange: range of time to visualize

        generates: a JSON object for the visualization
    """

    # Set default timezone
    tzDefault = cal.events[0].startTime.tzinfo

    # print tzDefault

    # Take user input for dates
    if dateRange == None:
        visRange = (datetime.datetime(2016, 5, 2, tzinfo=tzDefault), datetime.datetime(2016, 5, 8, tzinfo=tzDefault))
    else:
        visRange = dateRange

    #force them offset-aware
    visRange = (visRange[0].replace(tzinfo=tzDefault), visRange[1].replace(tzinfo=tzDefault))


    # Find the length of the vis in days
    visDelta = (visRange[1] - visRange[0])
    visLen = visDelta.days
    if visDelta.seconds > 0 or visDelta.microseconds > 0:
        visLen += 1

    # Set up list of days to process, including the day after it ends
    daysIncluded = [visRange[0] + i*datetime.timedelta(1) for i in range(visLen + 2)]

    #force these offset-awarae as well
    for dt in daysIncluded:
        dt.replace(tzinfo=tzDefault)
        # print dt.tzname()

    # Make labels
    dayStrings = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    labels = [1,2,3,4,5,6,7]

    # Initialize data dictionary with index values
    data = {'index': labels}

    for day in daysIncluded:
        print str(day.month) + '/' + str(day.day),
    print '\n'
    for event in cal.events:
        print str(event.startTime.month) + '/' + str(event.startTime.day),

    # Clean data (no date objects allowed) and accumulate total time
    for i in range(visLen):
        for event in cal.events:
            if not type(event.startTime) == datetime.datetime: # or not event.startTime.tzinfo:
                pass
            else:
                event.startTime.replace(tzinfo=tzDefault)
                event.endTime.replace(tzinfo=tzDefault)
                # print event.startTime.tzname(), event.endTime.tzname(), daysIncluded[i].tzname()
                if event.startTime >= daysIncluded[i] and event.startTime < daysIncluded[i+1]:
                    if not data.get(event.name):
                        data[event.name] = [0 for day in range(len(daysIncluded)-1)]
                    data[event.name][i] += event.duration.seconds / 60.0**2

    print data

    # Dictionary of plotting functions
    vizzes = {u'stackedArea':stackedArea, u'donut':donut, u'busy':busy}

    # Make plot
    print visualization
    print vizzes[visualization]
    plot = vizzes[visualization](data)

    # Generate JSON object to render in HTML template
    # plot.to_json('app/static/uploads/vis.json')
    plot.to_json('app/static/uploads/vis.json', html_out=True, html_path='app/static/uploads/vis.html')

def stackedArea(data):
    """ Creates a stacked area plot visualization """

    stacked = vincent.StackedArea(data, iter_idx='index', width=550)
    stacked.legend(title='Categories')
    stacked.colors(brew='Spectral')
    stacked.axis_titles(x='Day of the Week',y='Hours')
    return stacked


def donut(data):
    """ Creates a donut plot visualization """

    # Total the time in each category and give it back as a Pandas dataframe
    data = totalTime(data)
    donut = vincent.Pie(data, inner_radius=200, width=550)
    donut.colors(brew="Spectral")
    donut.legend('Categories')
    return donut


def busy(data):
    """ Creates a binary busy/free visualization """

    data = totalTime(data)
    busyTime = sum(data.values())
    unbusyTime = 7*24 - busyTime # 7 days * 24 hours/day
    business = {'unbusy':unbusyTime, 'busy':busyTime}
    print business
    busy = vincent.Pie(business, width=550)
    print busy
    busy.colors(brew='BW')
    busy.legend(title="business")
    return busy


def totalTime(data):
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

    visualize('softdes.ics', busy)
    try:
        name = sys.argv[1]
    except IndexError:
        name = 'stackedArea'
    visualize('Gaby.ics', name)
