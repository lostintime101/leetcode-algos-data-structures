import unittest

"""

Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

Constraints:

2 <= n <= 58

"""


class Solution:
    def integerBreak(self, n: int) -> int:

        # edge cases
        if n == 2: return 1
        if n == 3: return 2

        ans = 1
        while n > 2:
            n -= 3
            ans *= 3

        if n == 1:
            return (ans // 3) * 4

        if n == 2:
            return ans * 2

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_integer_break_with_two(self):
        self.assertEqual(self.solution.integerBreak(2), 1)

    def test_integer_break_with_three(self):
        self.assertEqual(self.solution.integerBreak(3), 2)

    def test_integer_break_with_four(self):
        # 4 can be split into 2 + 2, and the product is 4
        self.assertEqual(self.solution.integerBreak(4), 4)

    def test_integer_break_with_five(self):
        # 5 can be split into 2 + 3, and the product is 6
        self.assertEqual(self.solution.integerBreak(5), 6)

    def test_integer_break_with_ten(self):
        # 10 can be split into 3 + 3 + 4, and the product is 36
        self.assertEqual(self.solution.integerBreak(10), 36)

    def test_integer_break_with_large_number(self):
        # Testing with a larger number, expect a positive integer result
        self.assertGreater(self.solution.integerBreak(20), 0)


if __name__ == "__main__":
    unittest.main()
