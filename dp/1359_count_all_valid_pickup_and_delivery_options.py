import unittest

"""

Given n orders, each order consist in pickup and delivery services. 

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 

Since the answer may be too large, return it modulo 10^9 + 7.

Constraints:

1 <= n <= 500

"""


class Solution:
    def countOrders(self, n: int) -> int:

        factors = {1: 1}
        for i in range(2, (n * 2) + 2):
            factors[i] = factors[i - 1] + i

        curr = 0
        dp = [0] * n
        dp[0] = 1

        while curr != n - 1:
            curr += 1
            positions = (curr * 2) + 1
            factor = factors[positions]
            dp[curr] = (factor * dp[curr - 1])

        return dp[-1] % (10 ** 9 + 7)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_countOrders_1(self):
        # Test when n is 1
        self.assertEqual(self.solution.countOrders(1), 1)

    def test_countOrders_2(self):
        # Test when n is 2
        self.assertEqual(self.solution.countOrders(2), 6)

    def test_countOrders_3(self):
        # Test when n is 3
        self.assertEqual(self.solution.countOrders(3), 90)

    def test_countOrders_4(self):
        # Test when n is 4
        self.assertEqual(self.solution.countOrders(4), 2520)

    def test_countOrders_5(self):
        # Test when n is 5
        self.assertEqual(self.solution.countOrders(5), 113400)


if __name__ == '__main__':
    unittest.main()
