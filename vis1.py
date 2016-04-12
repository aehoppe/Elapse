""" Elapse
    SoftDes Final Project

    Visualization 1

    author: Gaby Clarke, Alex Hoppe
"""
import vincent
import elapseCalendar
import datetime
import os


c = elapseCalendar.Calendar('vis1cal')
c.parse_ical('Gaby')
# c.events.sort()

tzDefault = c.events[0].startTime.tzinfo
visRange = [datetime.datetime(2016, 3, 28, tzinfo=tzDefault), datetime.datetime(2016, 4, 3, tzinfo=tzDefault)]

daysIncluded = [visRange[0] + i*datetime.timedelta(1) for i in range(8)]
print daysIncluded
dayStrings = [str(i) for i in range(len(daysIncluded)-1)]


# data = {'index': daysIncluded[:-1]}
data = {'index': dayStrings}

for i in range(7):
    for event in c.events:
        if type(event.startTime) is datetime.date:
            continue
        event.startTime.replace(tzinfo=tzDefault)
        event.endTime.replace(tzinfo=tzDefault)
        print event.startTime.tzinfo
        if event.startTime >= daysIncluded[i] and event.startTime < daysIncluded[i+1]:
            if not data.get(event.name):
                data[event.name] = [0 for day in range(len(daysIncluded)-1)]
            data[event.name][i] += event.duration.seconds / 60.0**2

print data


stacked = vincent.StackedArea(data, iter_idx='index')
stacked.axis_titles(x='Index', y='Data Value')
stacked.legend(title='Categories')
stacked.colors(brew='Spectral')
stacked.to_json('vis1.json', html_out=True, html_path='vis1.html')

os.system("open vis1.html")
