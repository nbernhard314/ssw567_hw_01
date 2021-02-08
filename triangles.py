import unittest     # this makes Python unittest module available

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
        tri="Isoceles"
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
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testInts(self): # test integer inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(classifyTriangle(3,4,5),'Scalene, Right','3,4,5 should be a Scalene, Right triangle')
        self.assertNotEqual(classifyTriangle(4,4,4), 'Isoceles, Not Right', '4,4,4 should be an Equilateral, Not Right triangle.')

    def testFloats(self): #test float inputs
        self.assertEqual(classifyTriangle(0.125, 0.125, 0.125), 'Equilateral, Not Right', 'This is a 45,45,90 Isoceles Right triangle.')
        self.assertEqual(classifyTriangle(0.6, 0.8, 1), 'Scalene, Right', 'Decimal version of a 3,4,5 right triangle.')

    def testInvalidTypes(self): #test string, boolean, and null input
        self.assertNotEqual(classifyTriangle(True, False, False), 'Isoceles, Not Right', "Boolean input should throw an error")
        self.assertNotEqual(classifyTriangle(True, True, True), 'Equilteral, Not Right', "Boolean input should throw an error")
        self.assertNotEqual(classifyTriangle(False, False, False), 'Equilateral, Not Right', "Boolean input should throw an error")
        self.assertNotEqual(classifyTriangle(None, None, None), "Equilateral, Not Right", "None input should throw error")
        
        

if __name__ == '__main__':    
    unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
    
    
       
       