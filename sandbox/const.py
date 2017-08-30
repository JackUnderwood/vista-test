import sys
__author__ = 'Alex Martelli, revisions by John Underwood'
""" 
Once an attribute (constant) is bound, the item cannot be rebind or unbind.
See Python Cookbook, see recipe 6.2 Defining Constants
"""


class Const(object):
    class ConstError(TypeError):
        pass

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise self.ConstError("Can't rebind const({})".format(key))
        self.__dict__[key] = value

    def __delattr__(self, item):
        if item in self.__dict__:
            raise self.ConstError("Can't unbind const({})".format(item))
        raise NameError(item)


sys.modules[__name__] = Const()
