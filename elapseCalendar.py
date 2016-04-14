""" Elapse
    SoftDes Final Project

    author: Gaby Clarke, Alex Hoppe
"""

import icalendar
import Event as event
import os


class Calendar(object):
    """ An object with calendar information and a list of Event objects. """    
    
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

    def parse_ical(self, filename):
        """ Parses an ical (.ics) file, and populates Calendar.events with Event objects.

            filename: ical file to be parsed
        """
        f = open(filename)
        cal = icalendar.cal.Component.from_ical(''.join([l for l in f]))
        vevent_list = cal.walk(name='VEVENT')
        for vevent in vevent_list:
            e = event.Event(vevent)
            self.events.append(e)


if __name__ == '__main__':
    c = Calendar('Gaby.ics')
    print c.__repr__()