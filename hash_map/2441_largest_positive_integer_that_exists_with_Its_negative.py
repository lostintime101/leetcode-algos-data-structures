import unittest
from typing import List
from collections import Counter

"""

Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

Return the positive integer k. If there is no such integer, return -1.

Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
nums[i] != 0

"""

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        count = Counter(nums)
        possible = [k for k in count.keys() if k * -1 in count]
        possible.append(-1)
        return max(possible)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_findMaxK_single(self):
        nums = [1]
        self.assertEqual(self.solution.findMaxK(nums), -1)

    def test_findMaxK_positive(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.findMaxK(nums), -1)

    def test_findMaxK_negative(self):
        nums = [-1, -2, -3, -4, -5]
        self.assertEqual(self.solution.findMaxK(nums), -1)

    def test_findMaxK_mixed(self):
        nums = [-1, 2, -3, 4, -5]
        self.assertEqual(self.solution.findMaxK(nums), -1)

    def test_findMaxK_duplicates(self):
        nums = [1, 1, 2, 2, 3, 3]
        self.assertEqual(self.solution.findMaxK(nums), -1)

    def test_findMaxK_empty(self):
        nums = []
        self.assertEqual(self.solution.findMaxK(nums), -1)


if __name__ == '__main__':
    unittest.main()
