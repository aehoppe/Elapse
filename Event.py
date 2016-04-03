""" Elapse
    SoftDes Final Project

    author: Gaby Clarke, Alex Hoppe
"""

class Event(object):

    def __init__(self, vevent, name=None, importance=None):
        self.name = name
        # self.timeZone = timeZone
        # self.startTime = startTime
        # self.endTime = endTime
        # self.duration = duration
        # self.location = location
        self.importance = importance
        if vevent:
            self.name = vevent.decoded('summary')
            # self.timeZone = vevent.decoded('tzid')
            self.startTime = vevent.decoded('dtstart')
            self.endTime = vevent.decoded('dtend')
            self.duration = self.endTime - self.startTime
            # self.location

    def __repr__(self):
        return 'Event {}: start time:{}, end time:{}, duration:{}, location:{}, importance:{}'.format(self.name, self.timeZone, self.startTime, self.endTime, self.duration, self.location, self.importance)
