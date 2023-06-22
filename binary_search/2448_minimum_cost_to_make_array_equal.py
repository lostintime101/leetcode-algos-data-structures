import unittest
from typing import List

"""

You are given two 0-indexed arrays nums and cost consisting each of n positive integers.

You can do the following operation any number of times:

Increase or decrease any element of the array nums by 1.
The cost of doing one operation on the ith element is cost[i].

Return the minimum total cost such that all the elements of the array nums become equal.

Constraints:

n == nums.length == cost.length
1 <= n <= 105
1 <= nums[i], cost[i] <= 106

"""

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:

        sorted_nums = sorted(list(set(nums)))
        l, r = 0, len(sorted_nums) - 1

        def calculate_cost(targ):
            total = 0
            for i, v in enumerate(nums): total += abs(v - targ) * cost[i]
            return total

        while l <= r:

            mid = (l + r) // 2
            guess, lower, higher = 0, float("inf"), float("inf")

            guess = calculate_cost(sorted_nums[mid])
            if mid != 1: lower = calculate_cost(sorted_nums[mid - 1])
            if mid != len(sorted_nums) - 1: higher = calculate_cost(sorted_nums[mid + 1])

            # print(mid, sorted_nums[mid], guess, lower, higher)
            if guess == 0: return 0

            if (guess < lower) and (guess < higher):
                return guess
            elif (guess < lower):
                l = mid + 1
            else:
                r = mid - 1

        return min(guess, lower, higher)




class MinCostTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minCost_example1(self):
        nums = [1, 2, 3, 4, 5]
        cost = [3, 2, 1, 4, 5]
        self.assertEqual(self.solution.minCost(nums, cost), 19)

    def test_minCost_example2(self):
        nums = [7, 3, 5, 2, 8]
        cost = [10, 2, 4, 6, 7]
        self.assertEqual(self.solution.minCost(nums, cost), 53)

    def test_minCost_duplicateNumbers(self):
        nums = [1, 1, 2, 2, 3, 3]
        cost = [1, 2, 3, 4, 5, 6]
        self.assertEqual(self.solution.minCost(nums, cost), 13)

    def test_minCost_negativeNumbers(self):
        nums = [-5, -3, -1, 0, 2]
        cost = [5, 3, 1, 4, 2]
        self.assertEqual(self.solution.minCost(nums, cost), 34)

if __name__ == '__main__':
    unittest.main()

