""" Elapse
    SoftDes Final Project

    author: Gaby Clarke, Alex Hoppe
"""

def Event(object):

    def __init__(self, vevent, name=None, importance=None):
        self.name = name
        # self.timeZone = timeZone
        # self.startTime = startTime
        # self.endTime = endTime
        # self.duration = duration
        # self.location = location
        self.importance = importance
        if vevent:
            self.name = vevent['summary']
            self.timeZone = vevent['dtstart']
            self.startTime = vevent['dtstart']
            self.endTime = vevent['dtend']
            self.duration = self.endTime - self.startTime
            # self.location

    def __repr__(self):
        return 'Event {}: timezone:{}, start time:{}, end time:{}, duration:{}, location:{}, importance:{}'.format(self.name, self.timeZone, self.startTime, self.endTime, self.duration, self.location, self.importance)
