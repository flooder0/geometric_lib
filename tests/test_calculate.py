import unittest

from calculate import calc

class test_calculator(unittest.TestCase):
    def test_circle_perimeter(self):
        self.assertAlmostEqual(calc("circle", "perimeter", [5]),31.41592653589793, "Error in Perimeter calculating")
    def test_square_perimeter(self):
        self.assertEqual (calc("square", "perimeter", [4]),16, "Error in Perimeter calculating")
    def test_triangle_perimeter(self):
        self.assertEqual (calc("triangle", "perimeter", [3, 4, 5]), 12, "Error in Perimeter calculating")
    def test_circle_area(self):
        self.assertAlmostEqual (calc("circle", "area", [5]), 78.53981633974483, "Error in Area calculating")
    def test_square_area(self):
        self.assertEqual (calc("square", "area", [4]), 16, "Error in Area calculating")
    def test_triangle_area(self):
        self.assertAlmostEqual (calc("triangle", "area", [3, 4, 5]), 6, "Error in Area calculating")

if __name__ == '__main__':
    unittest.main()
