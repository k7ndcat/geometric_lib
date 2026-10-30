import sys

import math
import unittest
import circle
import rectangle
import square
import triangle

class CircleTestCase(unittest.TestCase):
    def test_negative_area(self):
        self.assertNotEqual(circle.area(-1), math.pi)

    def test_negative_perem(self):
        self.assertNotEqual(circle.perimeter(-1), math.pi * 2 * -1)

    def test_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    def test_area_one_rad(self):
        self.assertAlmostEqual(circle.area(1), math.pi, delta=0.00001)

    def test_area_one_point_rad(self):
        self.assertAlmostEqual(circle.area(1.0), math.pi, delta=0.00001)

    def test_area_half_rad(self):
        self.assertAlmostEqual(circle.area(0.5), math.pi / 4, delta=0.00001)

    def test_area_0_3_rad(self):
        self.assertAlmostEqual(circle.area(0.3), 0.09 * math.pi, delta=0.00001)

    def test_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_perimeter_positive(self):
        self.assertAlmostEqual(circle.perimeter(3), 6 * math.pi, delta=0.00001)

    def test_perimeter_fractional(self):
        self.assertAlmostEqual(circle.perimeter(0.5), math.pi, delta=0.00001)

    def test_area_diff_type_1(self):
        res = circle.area(2)
        self.assertAlmostEqual(res, 4 * math.pi, delta=0.00001)
        self.assertIs(type(res), float)

    def test_area_diff_type_2(self):
        res = circle.area(2.0)
        self.assertAlmostEqual(res, 4 * math.pi, delta=0.00001)
        self.assertIs(type(res), float)

    def test_area_diff_type_3(self):
        res = circle.area(0.0)
        self.assertAlmostEqual(res, 0 * math.pi, delta=0.00001)
        self.assertIs(type(res), float)

    def test_perimeter_diff_type_1(self):
        res = circle.perimeter(2)
        self.assertAlmostEqual(res, 4 * math.pi, delta=0.00001)
        self.assertIs(type(res), float)

    def test_perimeter_diff_type_2(self):
        res = circle.perimeter(2.0)
        self.assertAlmostEqual(res, 4 * math.pi, delta=0.00001)
        self.assertIs(type(res), float)

    def test_area_overflow_positive(self):
        maximum = sys.float_info.max
        res = circle.area(maximum)
        self.assertEqual(res, math.inf)

    def test_area_overflow_negative(self):
        maximum = sys.float_info.max
        res = circle.area(-maximum)
        self.assertEqual(res, math.inf)

    def test_perimeter_overflow_positive(self):
        maximum = sys.float_info.max
        res = circle.perimeter(maximum)
        self.assertEqual(res, math.inf)

    def test_perimeter_overflow_negative(self):
        maximum = sys.float_info.max
        res = circle.perimeter(-maximum)
        self.assertEqual(res, -math.inf)


class TriangleTestCase(unittest.TestCase):

    def test_area_negative(self):
        self.assertNotEqual(triangle.area(-3, -4), 6)

    def test_negative_perimeter(self):
        self.assertNotEqual(triangle.perimeter(-3, -4, -5), -12)

    def test_area_zero_height(self):
        self.assertEqual(triangle.area(5, 0), 0)

    def test_area_positive(self):
        self.assertEqual(triangle.area(3, 4), 6)

    def test_area_fractional(self):
        self.assertAlmostEqual(triangle.area(0.3, 0.4), 0.06, delta=0.00001)

    def test_perimeter_different_sides(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

    def test_perimetr_non_integ_true(self):
        self.assertNotEqual(triangle.perimeter(1.0, 1.0, 1.0), 3)

    def test_perimeter_float_result_type(self):
        res = triangle.perimeter(1.0, 1.0, 1.0)
        self.assertEqual(res, 3.0)
        self.assertIs(type(res), float)

    def test_perimeter_equal_sides(self):
        self.assertEqual(triangle.perimeter(5, 5, 5), 15)

    def test_perimeter_fractional(self):
        self.assertAlmostEqual(triangle.perimeter(0.3, 0.4, 0.5), 1.2, delta=0.00001)

    def test_area_diff_type_1(self):
        res = triangle.area(3, 4)
        self.assertAlmostEqual(res, 6, delta=0.00001)
        self.assertIs(type(res), int)

    def test_area_diff_type_2(self):
        res = triangle.area(3.0, 4.0)
        self.assertAlmostEqual(res, 6, delta=0.00001)
        self.assertIs(type(res), float)

    def test_area_diff_type_3(self):
        res = triangle.area(3, 4.0)
        self.assertAlmostEqual(res, 6, delta=0.00001)
        self.assertIs(type(res), float)

    def test_perimeter_diff_type_1(self):
        res = triangle.perimeter(3, 4, 5)
        self.assertAlmostEqual(res, 12, delta=0.00001)
        self.assertIs(type(res), int)

    def test_perimeter_diff_type_2(self):
        res = triangle.perimeter(3.0, 4.0, 5.0)
        self.assertAlmostEqual(res, 12, delta=0.00001)
        self.assertIs(type(res), float)

    def test_perimeter_diff_type_3(self):
        res = triangle.perimeter(3, 4.0, 5)
        self.assertAlmostEqual(res, 12, delta=0.00001)
        self.assertIs(type(res), float)

    def test_area_overflow_positive(self):
        maximum = sys.float_info.max
        res = triangle.area(maximum, maximum)
        self.assertEqual(res, math.inf)

    def test_area_overflow_negative(self):
        maximum = sys.float_info.max
        res = triangle.area(-maximum, -maximum)
        self.assertEqual(res, math.inf)

    def test_perimeter_overflow_positive(self):
        maximum = sys.float_info.max
        res = triangle.perimeter(maximum, maximum, maximum)
        self.assertEqual(res, math.inf)

    def test_perimeter_overflow_negative(self):
        maximum = sys.float_info.max
        res = triangle.perimeter(-maximum, -maximum, -maximum)
        self.assertEqual(res, -math.inf)

class RectangleTestCase(unittest.TestCase):

    def test_negative_area(self):
        self.assertNotEqual(rectangle.area(-3, -4), 12)

    def test_negative_perimeter(self):
        self.assertNotEqual(rectangle.perimeter(-3, -4), -14)

    def test_zero_mul(self):
        self.assertEqual(rectangle.area(10, 0), 0)

    def test_square_mul(self):
        self.assertEqual(rectangle.area(10, 10), 100)

    def test_area_different_sides(self):
        self.assertEqual(rectangle.area(3, 4), 12)

    def test_area_fractional_sides(self):
        self.assertAlmostEqual(rectangle.area(0.1, 0.2), 0.02, delta=0.00001)

    def test_perimeter_different_sides(self):
        self.assertEqual(rectangle.perimeter(3, 4), 14)

    def test_perimeter_equal_sides(self):
        self.assertEqual(rectangle.perimeter(10, 10), 40)

    def test_perimeter_fractional_sides(self):
        self.assertAlmostEqual(rectangle.perimeter(0.1, 0.2), 0.6, delta=0.00001)

    def test_area_diff_type_1(self):
        res = rectangle.area(3, 4)
        self.assertAlmostEqual(res, 12, delta=0.00001)
        self.assertIs(type(res), int)

    def test_area_diff_type_2(self):
        res = rectangle.area(3.0, 4.0)
        self.assertAlmostEqual(res, 12, delta=0.00001)
        self.assertIs(type(res), float)

    def test_area_diff_type_3(self):
        res = rectangle.area(3, 4.0)
        self.assertAlmostEqual(res, 12, delta=0.00001)
        self.assertIs(type(res), float)

    def test_perimeter_diff_type_1(self):
        res = rectangle.perimeter(3, 4)
        self.assertAlmostEqual(res, 14, delta=0.00001)
        self.assertIs(type(res), int)

    def test_perimeter_diff_type_2(self):
        res = rectangle.perimeter(3.0, 4.0)
        self.assertAlmostEqual(res, 14, delta=0.00001)
        self.assertIs(type(res), float)

    def test_perimeter_diff_type_3(self):
        res = rectangle.perimeter(3, 4.0)
        self.assertAlmostEqual(res, 14, delta=0.00001)
        self.assertIs(type(res), float)

    def test_area_ans_noteq_type(self):
        res = rectangle.area(3.0, 4.0)
        self.assertNotEqual(res, 12)

    def test_perimeter_ans_enoteq_type(self):
        res = rectangle.perimeter(3.0, 4.0)
        self.assertNotEqual(res, 14)

    def test_area_overflow_positive(self):
        maximum = sys.float_info.max
        res = rectangle.area(maximum, maximum)
        self.assertEqual(res, math.inf)

    def test_area_overflow_negative(self):
        maximum = sys.float_info.max
        res = rectangle.area(-maximum, -maximum)
        self.assertEqual(res, math.inf)

    def test_perimeter_overflow_positive(self):
        maximum = sys.float_info.max
        res = rectangle.perimeter(maximum, maximum)
        self.assertEqual(res, math.inf)

    def test_perimeter_overflow_negative(self):
        maximum = sys.float_info.max
        res = rectangle.perimeter(-maximum, -maximum)
        self.assertEqual(res, -math.inf)

class SquareTestCase(unittest.TestCase):

    def test_negative_area(self):
        self.assertNotEqual(square.area(-2), 4)

    def test_negative_perimeter(self):
        self.assertNotEqual(square.perimeter(-2), -8)

    def test_area_zero(self):
        self.assertEqual(square.area(0), 0)

    def test_area_positive(self):
        self.assertEqual(square.area(5), 25)

    def test_area_fractional(self):
        self.assertAlmostEqual(square.area(0.3), 0.09, delta=0.00001)

    def test_perimeter_zero(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_perimeter_positive(self):
        self.assertEqual(square.perimeter(5), 20)

    def test_perimeter_fractional(self):
        self.assertAlmostEqual(square.perimeter(0.3), 1.2, delta=0.00001)

    def test_area_diff_type_1(self):
        res = square.area(5)
        self.assertAlmostEqual(res, 25, delta=0.00001)
        self.assertIs(type(res), int)

    def test_area_diff_type_2(self):
        res = square.area(5.0)
        self.assertAlmostEqual(res, 25, delta=0.00001)
        self.assertIs(type(res), float)

    def test_perimeter_diff_type_1(self):
        res = square.perimeter(5)
        self.assertAlmostEqual(res, 20, delta=0.00001)
        self.assertIs(type(res), int)

    def test_perimeter_diff_type_2(self):
        res = square.perimeter(5.0)
        self.assertAlmostEqual(res, 20, delta=0.00001)
        self.assertIs(type(res), float)

    def test_area_ans_noteq_type(self):
        res = square.area(2.0)
        self.assertEqual(res, 4)

    def test_perimeter_ans_noteq_type(self):
        res = square.perimeter(2.0)
        self.assertNotEqual(res, 8)

    def test_area_overflow_positive(self):
        maximum = sys.float_info.max
        res = square.area(maximum)
        self.assertEqual(res, math.inf)

    def test_area_overflow_negative(self):
        maximum = sys.float_info.max
        res = square.area(-maximum)
        self.assertEqual(res, math.inf)

    def test_perimeter_overflow_positive(self):
        maximum = sys.float_info.max
        res = square.perimeter(maximum)
        self.assertEqual(res, math.inf)

    def test_perimeter_overflow_negative(self):
        maximum = sys.float_info.max
        res = square.perimeter(-maximum)
        self.assertEqual(res, -math.inf)
