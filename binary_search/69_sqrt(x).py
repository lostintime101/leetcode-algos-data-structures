import unittest

"""

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Constraints:

0 <= x <= 231 - 1

"""

class Solution:
    def mySqrt(self, x: int) -> int:

        # BUILT-IN FUNCTIONS
        # return floor(sqrt(x))

        # BINARY SEARCH

        l, r = 0, x

        while l <= r:

            mid = (l + r) // 2
            result = mid * mid
            next_result = (mid + 1) * (mid + 1)

            if result == x:
                return mid
            elif result > x:
                r = mid - 1
            elif next_result > x:
                return mid
            else:
                l = mid + 1

        return 0
    

class TestMySqrt(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_example_1(self):
        x = 4
        expected_output = 2
        self.assertEqual(self.s.mySqrt(x), expected_output)

    def test_example_2(self):
        x = 8
        expected_output = 2
        self.assertEqual(self.s.mySqrt(x), expected_output)

    def test_perfect_square(self):
        x = 16
        expected_output = 4
        self.assertEqual(self.s.mySqrt(x), expected_output)

    def test_not_perfect_square(self):
        x = 10
        expected_output = 3
        self.assertEqual(self.s.mySqrt(x), expected_output)

    def test_zero_input(self):
        x = 0
        expected_output = 0
        self.assertEqual(self.s.mySqrt(x), expected_output)


if __name__ == '__main__':
    unittest.main()
