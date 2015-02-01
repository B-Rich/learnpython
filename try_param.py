#! /usr/bin/python
## this a python file for 6.4.6

def story(**kwds):
    return 'Once upon a time, there is a ' \
        '%(job)s called %(name)s.' % kwds

def power(x, y, *others):
    if others:
        print 'Received redundant parameters:'. others
    return pow(x,y)

def interval(start, stop=None, step=1):
    'Imitates range() for step > 0'
    if stop is None:
        start, stop = 0, start
    result = []
    i =start
    while 1 < stop:
        result.append(i)
        i += step
    return result
