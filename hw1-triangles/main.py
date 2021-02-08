# -*- coding: utf-8 -*-
"""
Created on Feb 8th, 2020

@author: Tim Leonard
"""

import unittest     # this makes Python unittest module available

def classifyTriangle(a,b,c):
    """
    
    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
    """
    if a <= 0 or b <= 0 or c <= 0:
       return 'NotATriangle' 
    elif a == b and b == c:
       return 'Equilateral'
    elif a*a + b*b == c*c or b*b + c*c == a*a or a*a + c*c == b*b:
      return 'Right'
    elif (a == b and a != c) or (b == c and b != a) or (a == c and a != b):
      return 'Isoceles'
    elif a != b and a != c:
      return 'Scalene'
    else:
      return 'NotATriangle'
        
        
def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,c),sep="")
# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testSet1(self): # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(0, 2, 8), 'NotATriangle', 'Should be NotATriangle')
        self.assertEqual(classifyTriangle(6,8,10), 'Right', 'Should be Right')
        self.assertEqual(classifyTriangle(5, 10, 10), 'Isoceles', 'Should be Isoceles')
        self.assertNotEqual(classifyTriangle(0,0,0), 'Equilateral', 'Should be NotATriangle')
        
    def testMyTestSet2(self): 
        # define multiple test sets to test different aspects of the code
        # notice that tests can have bugs too!
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertNotEqual(classifyTriangle(10,10,10),'Isoceles','Should be Equilateral')
        self.assertEqual(classifyTriangle(10,15,30),'Scalene','Should be Scalene')
        

if __name__ == '__main__':
    # examples of running the code
    runClassifyTriangle(1,2,3)
    runClassifyTriangle(1,1,1)
    #unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
    
    
       
       
