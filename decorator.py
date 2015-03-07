#!/usr/bin python
'''
@deco2
@deco1
def func(arg):
    pass

## Equal
def func(arg):
    pass
func = deco2(deco1(func))
'''
from time import ctime,sleep

def tsfunc(func):
    def wrappedFunc():
        print '[%s] %s called' %(ctime(), func.__name__)
        return func()

    return wrappedFunc
  
@tsfunc
def foo():
    pass

foo()
sleep(4)

for i in range(2):
    sleep(1)
    foo()
