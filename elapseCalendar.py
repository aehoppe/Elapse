""" Elapse
    SoftDes Final Project

    author: Gaby Clarke, Alex Hoppe
"""
import icalendar
import Event as event

class Calendar(object):
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
        f = open(filename+'.ics')
        cal = icalendar.cal.Component.from_ical(''.join([l for l in f]))
        vevent_list = cal.walk(name='VEVENT')
        # print str(vevent_list) + 'vevent list'
        for vevent in vevent_list:
            e = event.Event(vevent)
            self.events.append(e)

if __name__ == '__main__':
    c = Calendar('softdestest')
    c.parse_ical('softdes')
    # try:
    #     print c.__repr__()
    # except:
    #     print 'repr failed'
    print c
