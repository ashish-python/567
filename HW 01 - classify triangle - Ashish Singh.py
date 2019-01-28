'''
author: Ashish Singh

- Function classify_triangle() returns the type of triangle. It tests if the values provided are valid, if the values 
can form a triangle.

- class TestSuite includes test function test_classify_traingle() that raises exception if the values provided are not valid
It also tests if the function classify_triangle correctly identifies the type of triangle.
'''
import unittest

def classify_triangle(a,b,c):
    '''
    Return a string identifying the type of triangle
    
    Raise exception if the input entries are invalid in any way - any side below zero, cannot be type converted to float
    or the entries cannot form a triangle

    '''
    
    #Check if values can be converted to float numbers. If yes, round the values. If No, raise exception
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except:
        raise ValueError("ERROR: Triangle sides have to be numbers")
    else:
        a = round(a,2)
        b = round(b,2)
        c = round(c,2)

    #Confirm if all the values are larger than zero. If no, raise exception
    if(a<=0 or b<=0 or c<=0):
        raise ValueError("ERROR: Triangle sides length have to be larger than zero")
    

    #Check if this is a valid triangle. Sum of any two sides should be greater than the third side
    if(a+b<c or a+c<b or b+c<a):        
        raise ValueError("ERROR: Not a valid triangle. Sum of any two sides has to be greater than the third side")
        
    #No exceptions raised. Check what type of triangle it is and return the result

    triangle_type = list()
    lst = list((a,b,c))
    lst.sort()
    if(round((lst[0]**2+lst[1]**2)**(1/2),2)==lst[2]):
        triangle_type.append("Right")

    if(a!=b and b!=c and c!=a):
        triangle_type.append("scalene")

    if(a==b and b==c):
        triangle_type.append("equilateral")

    if(((a==b) and (a!=c)) or ((a==c) and (a!=b)) or ((a!=b) and (b==c))):
        triangle_type.append("isosceles")

    return ", ".join(triangle_type)


class TestSuite(unittest.TestCase):    
    '''
        Test class for classify_triangle()
        Tests included for a valid triangle, Right triangle, equilateral, isosceles and scalene
    '''
    #Test if it is a valid triangle. Sum of any two sides greater than the third side
    def test_classify_triangle(self):
        with self.assertRaises(ValueError):
            classify_triangle(1,5,1.1)

    #Test if all the values can be convered to float
        with self.assertRaises(ValueError):
            classify_triangle(1,1,"two")

    #Test if any of the sides is less than or equal to zero
        with self.assertRaises(ValueError):
            classify_triangle(1,1,-1)
        
        with self.assertRaises(ValueError):
            classify_triangle(0,4,5)

    #Right triangles - could be Right scalene or Right isosceles
        self.assertEqual(classify_triangle(5,4,3),"Right, scalene")
        self.assertEqual(classify_triangle(5,4,"3"),"Right, scalene")
        self.assertEqual(classify_triangle(5,"7.07",5),"Right, isosceles")
        self.assertEqual(classify_triangle(6.03,6.03,8.53),"Right, isosceles")

    
    #Scalene triangles - not Right triangle
        self.assertEqual(classify_triangle(5.2,3.66,4),"scalene")
        self.assertEqual(classify_triangle(5.2,5.22,"4"),"scalene")
        self.assertNotEqual(classify_triangle("6.4",6.4,6.46),"scalene")

    #Equilateral triangles
        self.assertEqual(classify_triangle(6.4,6.400,6.4),"equilateral")
        self.assertEqual(classify_triangle("6.4",6.404,6.4),"equilateral")
        self.assertEqual(classify_triangle("6.4","6.4",6.4),"equilateral")
        self.assertNotEqual(classify_triangle("6.4",6.406,6.4),"equilateral")

    #isosceles triangles - Not Right triangle
        self.assertEqual(classify_triangle(2.4,3,2.4),"isosceles")
        self.assertEqual(classify_triangle(2,4,"4"),"isosceles")
        self.assertEqual(classify_triangle(6.1,6.1,4),"isosceles")
        self.assertEqual(classify_triangle("6.4",6.406,6.4),"isosceles")

    #Change order of parameters 
        self.assertTrue(classify_triangle(5,2,6)==classify_triangle(2,6,5))

if __name__=="__main__":
    unittest.main(verbosity=2,exit=False)

# The following code asks the user to input the sides of the triangle. 
# If user entries are incorrect because of the format or the sides do not form a valid triangle an exception is raised. 
# If user entries are valid, the type of triangle is displayed

loop = True
while(loop):
    a = input("Enter side 'a' of triangle: ")
    b = input("Enter side 'b' of triangle: " )
    c = input("Enter side 'c' of triangle: ")

    try:
        triangle = classify_triangle(a,b,c)
    except ValueError as e:
        print(e)
    else:
        print()
        print("Triangle type:",triangle)
        loop = False



