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
        return "Not Right"
    else:
        return "Right"

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
    def testSet1(self): # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        
    def testMyTestSet2(self): 
        # define multiple test sets to test different aspects of the code
        # notice that tests can have bugs too!
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertNotEqual(classifyTriangle(10,10,10),'Isoceles','Should be Equilateral')
        self.assertEqual(classifyTriangle(10,15,30),'Scalene','Should be Isoceles')
        

if __name__ == '__main__':
    # examples of running the code
    runClassifyTriangle(1,2,3)
    runClassifyTriangle(1,1,1)
    
    #unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    #unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
    
    
       
       