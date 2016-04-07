""" Elapse
    SoftDes Final Project

    Visualization 1

    author: Gaby Clarke, Alex Hoppe
"""
import vincent
import elapseCalendar
import datetime


c = elapseCalendar.Calendar('vis1cal')
c.parse_ical('softdes')
print c
c.events.sort()
print c

tzDefault = c.events[0].startTime.tzinfo

visRange = [datetime.datetime(2016, 3, 28, tzinfo=tzDefault), datetime.datetime(2016, 4, 3, tzinfo=tzDefault)]

daysIncluded = [visRange[0] + i*datetime.timedelta(1) for i in range(8)]
print daysIncluded

data = {'index': daysIncluded}

for i in range(8):
    for event in c.events:
        if event.startTime >= daysIncluded[i] and event.startTime < daysIncluded[i+1]:
            if not data.get(event.name):
                data[event.name] = [datetime.timedelta(0) for day in range(len(daysIncluded)-1)]
            data[event.name][i] += event.duration

print data



# times = []
# for event in c.events:
#     if type(event.startTime) is datetime.datetime:
#         times.append(event.startTime)
#         times.append(event.endTime)

# times.sort()
# print times



# visEvents = []
# for event in c.events:
#     if event.startTime in visRange or event.endTime in visRange:
#         visEvents.append(event)


# calDelta = times[-1] - times[0]
# dayDelta = calDelta.days

# if calDelta.seconds or calDelta.microseconds:
#     dayDelta += 1
# print dayDelta




stacked = vincent.StackedArea(data, iter_idx='index')
stacked.axis_titles(x='Index', y='Data Value')
stacked.legend(title='Categories')
stacked.colors(brew='Spectral')
stacked.to_json('vis1.json', html_out=True, html_path='vis1.html')