import math
import unittest

"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
-104 <= xn <= 104

"""


class Solution:
    def myPow(self, x: float, n: int) -> float:

        # SIMPLE SOLUTIONS
        # return x ** n
        # return pow(x,n)

        # WORKS BUT TOO SLOW FOR n=2147483647

        if n == 0: return 1

        negative = False
        if n < 0: negative = True
        n = abs(n)

        xx = x

        for _ in range(n - 1): x = x * xx

        if negative: x = 1 / x

        return x


class TestMyPow(unittest.TestCase):

    def test_zero_power(self):
        self.assertEqual(Solution().myPow(2, 0), 1)
        self.assertEqual(Solution().myPow(3.14, 0), 1)
        self.assertEqual(Solution().myPow(0, 0), 1)

    def test_positive_power(self):
        self.assertEqual(Solution().myPow(2, 3), 8)
        self.assertAlmostEqual(Solution().myPow(1.5, 2), 2.25)
        self.assertEqual(Solution().myPow(10, 5), 100000)

    def test_negative_power(self):
        self.assertAlmostEqual(Solution().myPow(2, -3), 0.125)
        self.assertEqual(Solution().myPow(1.5, -2), 0.4444444444444444)
        self.assertAlmostEqual(Solution().myPow(10, -5), 0.00001)

    def test_large_power(self):
        self.assertAlmostEqual(Solution().myPow(2, 100), math.pow(2, 100))
        self.assertAlmostEqual(Solution().myPow(1.5, 200), math.pow(1.5, 200))
        self.assertAlmostEqual(Solution().myPow(10, 10), math.pow(10, 10))


if __name__ == '__main__':
    unittest.main()
