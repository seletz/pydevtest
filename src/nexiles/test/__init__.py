from java.lang import String

import os

class MyClass(object):
    def __init__(self, foo):
        self.foo = foo

if __name__ == "__main__":
    s = String("foo")
    i = MyClass(s)

    print i.foo