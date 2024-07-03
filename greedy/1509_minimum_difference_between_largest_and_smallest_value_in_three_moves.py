import unittest
from typing import List

"""

You are given an integer array nums.

In one move, you can choose one element of nums and change it to any value.

Return the minimum difference between the largest and smallest value of nums after performing at most three moves.

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109

"""

class Solution:
    def minDifference(self, nums: List[int]) -> int:

        N = len(nums)
        if N <= 3: return 0

        poss = [[0, -4], [1, -3], [2, -2], [3, -1]]

        ans = float("inf")
        nums = sorted(nums)

        for [start, end] in poss:
            ans = min(ans, abs(nums[end] - nums[start]))

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_cases(self):
        self.assertEqual(self.solution.minDifference([5, 3, 2, 4]), 0)
        self.assertEqual(self.solution.minDifference([1, 5, 0, 10, 14]), 1)
        self.assertEqual(self.solution.minDifference([6, 6, 0, 1, 1, 4, 6]), 2)
        self.assertEqual(self.solution.minDifference([1, 5, 6, 14, 15]), 1)

    def test_edge_cases(self):
        self.assertEqual(self.solution.minDifference([1]), 0)
        self.assertEqual(self.solution.minDifference([1, 2]), 0)
        self.assertEqual(self.solution.minDifference([1, 2, 3]), 0)
        self.assertEqual(self.solution.minDifference([1, 5, 9, 14]), 0)
        self.assertEqual(self.solution.minDifference([4, 5, 6, 7, 8]), 1)

    def test_large_values(self):
        self.assertEqual(self.solution.minDifference([1000, 2000, 3000, 10000, 100000]), 1000)
        self.assertEqual(self.solution.minDifference([100000, 1000000, 10000000, 100000000]), 0)

    def test_sorted_input(self):
        self.assertEqual(self.solution.minDifference([1, 2, 3, 4]), 0)
        self.assertEqual(self.solution.minDifference([10, 20, 30, 40]), 0)

    def test_reverse_sorted_input(self):
        self.assertEqual(self.solution.minDifference([40, 30, 20, 10]), 0)
        self.assertEqual(self.solution.minDifference([4, 3, 2, 1]), 0)


if __name__ == '__main__':
    unittest.main()