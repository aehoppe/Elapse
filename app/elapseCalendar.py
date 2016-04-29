""" Elapse
    SoftDes Final Project

    author: Gaby Clarke, Alex Hoppe
"""

import icalendar
import elapseEvent as event
import os
import datetime


class elapseCalendar(object):
    """ An object with calendar information and a list of elapseEvent objects. """

    def __init__(self, name, events=None):
        if events == None:
            events = []
        self.events = events
        self.name = name

    def __repr__(self):
        output = 'calendar {} \n'.format(self.name)
        for e in self.events:
            output += e.__repr__() + '\n'
        output += 'calendar {} end'.format(self.name)
        return output

    def parse_ical(self, filename, daterange=None):
        """ Parses an ical (.ics) file, and populates elapseCalendar.events with
            elapseEvent objects.

            filename: ical file to be parsed
        """
        f = open(filename)
        ical = icalendar.cal.Component.from_ical(''.join([l for l in f]))
        vevent_list = ical.walk(name='VEVENT')

        # Take user input for dates
        if daterange == None:
            visRange = (datetime.date(2016, 3, 28), datetime.date(2016, 4, 3))
        else:
            visRange = daterange

        for vevent in vevent_list:
            e = event.Event(vevent)
            if e.date <= visRange[1] and e.date >= visRange[0]:
                self.events.append(e)


if __name__ == '__main__':
    c = elapseCalendar('Gaby.ics')
    print c.__repr__()
