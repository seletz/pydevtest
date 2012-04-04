'''
Created on 04.04.2012

@author: seletz
'''
import unittest
from nexiles.test import MyClass


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMyClass(self):
        i = MyClass("x")
        
        self.assertEqual("x", i.foo, "NE")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testMyClass']
    unittest.main()