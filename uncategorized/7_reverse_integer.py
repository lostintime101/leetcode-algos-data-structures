import unittest

"""

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes
the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Constraints:

-231 <= x <= 231 - 1

"""


class Solution:
    def reverse(self, x: int) -> int:

        # SIMPLE SOLUTION

        string = str(x)[::-1]

        if string[-1] == "-":
            string = "-" + string
            string = string[:-1]

        if abs(int(string)) > 2147483647: return 0

        return int(string)


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_reverse(self):
        self.assertEqual(self.s.reverse(123), 321)
        self.assertEqual(self.s.reverse(-123), -321)
        self.assertEqual(self.s.reverse(120), 21)
        self.assertEqual(self.s.reverse(0), 0)
        self.assertEqual(self.s.reverse(1534236469), 0)
        self.assertEqual(self.s.reverse(-2147483648), 0)


if __name__ == '__main__':
    unittest.main()
