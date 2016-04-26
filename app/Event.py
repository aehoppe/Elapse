""" Elapse
    SoftDes Final Project

    author: Gaby Clarke, Alex Hoppe
"""

import datetime


class Event(object):
    """ An object with decoded event information from an ical event. """

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
        return 'Event {}: start time:{}, end time:{}, duration:{}'.format(self.name, self.startTime, self.endTime, self.duration)

    def __cmp__(self, other):
        """ Compares two Event objects based on start time."""
        if self.startTime > other.startTime:
            return 1
        elif self.startTime < other.startTime:
            return -1
        else:
            return 0