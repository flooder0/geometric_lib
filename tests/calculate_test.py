import unittest
from calculate import *

class testCalculator(unittest.TestCase):
    def test_circlePerimeter(self):
        self.assertAlmostEqual(calc("circle", "perimeter", [5]),31.41592653589793, "Error in Perimeter calculating")
    def test_squarePerimeter(self):
        self.assertEqual (calc("square", "perimeter", [4]),16, "Error in Perimeter calculating")
    def test_trianglePerimeter(self):
        self.assertEqual (calc("triangle", "perimeter", [3, 4, 5]), 12, "Error in Perimeter calculating")
    def test_circleArea(self):
        self.assertAlmostEqual (calc("circle", "area", [5]), 78.53981633974483, "Error in Area calculating")
    def test_squareArea(self):
        self.assertEqual (calc("square", "area", [4]), 16, "Error in Area calculating")
    def test_triangleArea(self):
        self.assertAlmostEqual (calc("triangle", "area", [3, 4, 5]), 6, "Error in Area calculating")


    #calc(fig, func, size)

if __name__ == '__main__':
    unittest.main()
