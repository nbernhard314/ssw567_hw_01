import unittest     # this makes Python unittest module available
import math

def checkRight(a, b, c):
    sides = a*a + b*b
    hyp = c*c
    if(a>b and a>c):
        sides = b*b + c*c
        hyp = a*a
    elif(b>a and b>c):
        sides = a*a + c*c
        hyp = b*b
    elif(c>a and c>b):
        sides = a*a + b*b
        hyp = c*c

    if(sides==hyp):
        return "Right"
    else:
        return "Not Right"

def classifyTriangle(a,b,c):
    tri = "Scalene"
    right = "Not Right"
    if(a == b and b == c):
        tri="Equilateral"
    elif(a == b or b == c or a == c):
        tri="Isosceles"
        right=checkRight(a, b, c)
    else:
        right=checkRight(a, b, c)

    return tri+", "+right

    
        
        
def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,c),sep="")


# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    def testValidInts(self): # test integer inputs
        # testing one of each possible triangle with ints
        self.assertEqual(classifyTriangle(3,4,5),'Scalene, Right','3,4,5 should be a Scalene, Right triangle')
        self.assertEqual(classifyTriangle(4,4,4), 'Equilateral, Not Right', '4,4,4 should be an Equilateral, Not Right triangle.')
        self.assertEqual(classifyTriangle(3,4,6), 'Scalene, Not Right', '3,4,6 should be a Scalene, Not Right triangle')
        self.assertEqual(classifyTriangle(3,4,3), 'Isosceles, Not Right', '3,4,3 should be an Isosceles, Not Right triangle')
        # testing order of right triangle input
        self.assertEqual(classifyTriangle(4,5,3), 'Scalene, Right', '4,5,3 should be a Scalene, Right triangle')
        # isosceles right triangles cannot be represented using python as all of these triangle types have at least 1 irrational side

    def testInvalidInts(self):
        # test with 0 and negative numbers as input; both should likely throw an error
        self.assertNotEqual(classifyTriangle(10, 12, 0), 'Scalene, Not Right', '10,12,0 should throw an error for having a side length of zero')
        self.assertNotEqual(classifyTriangle(-3,-4,-5), 'Scalene, Right', '-3,-4,-5 should throw an error for having negative measurements')

    def testValidFloats(self): #test float inputs
        # testing one of each possible triangle with ints
        self.assertEqual(classifyTriangle(0.125, 0.125, 0.125), 'Equilateral, Not Right', '0.125,0.125,0.125 should be an Equilateral, Not Right triangle')
        self.assertEqual(classifyTriangle(0.6, 0.8, 1), 'Scalene, Right', '0.6,0.8,1 should be a Scalene, Right triangle')
        self.assertEqual(classifyTriangle(1.32, 1.325, 1.33), 'Scalene, Not Right', '1.32,1.325,1.33 should be a Scalene, Not Right triangle')
        self.assertEqual(classifyTriangle(33.452, 30.521, 30.521), 'Isosceles, Not Right', '33.452,30.521,30.521 should be an Isosceles, Not Right triangle')
        # isosceles right triangles cannot be represented using python as all of these triangle types have at least 1 irrational side

    def testInvalidFloats(self):
        # test with 0 and negative numbers as input; both should likely throw an error
        self.assertNotEqual(classifyTriangle(30.052, 12.123, 0.000), 'Scalene, Not Right', '10,12,0 should throw an error for having a side length of zero')
        self.assertNotEqual(classifyTriangle(-3.054,-4.78320,-5.02093), 'Scalene, Not Right', '-3,-4,-5 should throw an error for having negative measurements')

    def testInvalidTypes(self): #test string, boolean, and null input
        self.assertNotEqual(classifyTriangle(True, False, False), 'Isoceles, Not Right', "Boolean input should throw an error")
        self.assertNotEqual(classifyTriangle(True, True, True), 'Equilteral, Not Right', "Boolean input should throw an error")
        self.assertNotEqual(classifyTriangle(False, False, False), 'Equilateral, Not Right', "Boolean input should throw an error")
        self.assertNotEqual(classifyTriangle(None, None, None), "Equilateral, Not Right", "None input should throw error")
        
        

if __name__ == '__main__':    
    unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
    
    
       
       