import unittest

"""

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

"""


class Solution:
    def maxProfit(self, prices) -> int:

        low, high, ret = 10000, 0, 0
        highs = []

        for i in range(len(prices)):

            if high < prices[len(prices) - (i + 1)]: high = prices[len(prices) - (i + 1)]
            highs.append(high)

        highs = highs[::-1]

        for i in range(len(prices)):
            low = min(low, prices[i])
            ret = max(ret, (highs[i] - low))

        return ret


class TestSolution(unittest.TestCase):

    def test_no_profit(self):
        prices = [5, 4, 3, 2, 1]
        solution = Solution()
        result = solution.maxProfit(prices)
        self.assertEqual(result, 0)

    def test_one_transaction(self):
        prices = [7, 1, 5, 3, 6, 4]
        solution = Solution()
        result = solution.maxProfit(prices)
        self.assertEqual(result, 5)

    def test_multiple_transactions(self):
        prices = [7, 1, 5, 3, 6, 4, 10]
        solution = Solution()
        result = solution.maxProfit(prices)
        self.assertEqual(result, 9)

    def test_empty_list(self):
        prices = []
        solution = Solution()
        result = solution.maxProfit(prices)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
