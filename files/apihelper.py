"""Cheap and simple API helper

This program is part of "Dive Into Python", a free Python book for
experienced programmers.  Visit http://diveintopython.org/ for the
latest version.
"""

__author__ = "Mark Pilgrim (mark@diveintopython.org)"
__version__ = "$Revision: 1.3 $"
__date__ = "$Date: 2004/05/05 21:57:19 $"
__copyright__ = "Copyright (c) 2001 Mark Pilgrim"
__license__ = "Python"

# While this is a good example script to teach about introspection,
# in real life it has been superceded by PyDoc, which is part of the
# standard library in Python 2.1 and later.
# 
# Your IDE may already import the "help" function from pydoc
# automatically on startup; if not, do this:
# 
# >>> from pydoc import help
# 
# The help function in this module takes the object itself to get
# help on, but PyDoc can also take a string, like this:
# 
# >>> help("string") # gets help on the string module
# >>> help("apihelper.help") # gets help on the function below
# >>> help() # enters an interactive help mode
# 
# PyDoc can also act as an HTTP server to dynamically produce
# HTML-formatted documentation of any module in your path.
# That's wicked cool.  Read more about PyDoc here:
#   http://www.onlamp.com/pub/a/python/2001/04/18/pydoc.html

def info(object, spacing=10, collapse=1):
	"""Print methods and doc strings.

	Takes module, class, list, dictionary, or string."""
        ## 所以这个表达式接收一个名为 object 的对象,然后得到它的属性、方法、函数 和其他成员的名称列表,接着过滤掉我们不关心的成员。执行过滤行为是通 过对每个属性/方法/函数的名称调用 getattr 函数取得实际成员的引用,然后 检查这些成员对象是否是可调用的,当然这些可调用的成员对象可能是方法 或者函数,同时也可能是内置的 (比如列表的 pop 方法) 或者用户自定义的 (比 如 odbchelper 模块的 buildConnectionString 函数)。这里你不用关心其它的属性,
	methodList = [e for e in dir(object) if callable(getattr(object, e))]
	processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
	print "\n".join(["%s %s" %
					 (method.ljust(spacing),
					  processFunc(str(getattr(object, method).__doc__)))
					 for method in methodList])

if __name__ == "__main__":
	print help.__doc__
