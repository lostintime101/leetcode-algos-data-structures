import unittest
from typing import List

"""

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104


"""


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        if len(nums) == 1: return nums[0] / k

        ret = float("-inf")
        curr = sum(nums[:k])
        ret = max(curr / k, ret)

        for i in range(len(nums) - k):
            curr -= nums[i]
            curr += nums[i + k]
            ret = max(curr / k, ret)

        return ret


class SolutionTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_findMaxAverage_example1(self):
        nums = [1, 12, -5, -6, 50, 3]
        k = 4
        expected = 12.75
        self.assertEqual(self.solution.findMaxAverage(nums, k), expected)

    def test_findMaxAverage_example2(self):
        nums = [5]
        k = 1
        expected = 5.0
        self.assertEqual(self.solution.findMaxAverage(nums, k), expected)

    def test_findMaxAverage_example3(self):
        nums = [0, 1, 1, 3, 3]
        k = 4
        expected = 2.0
        self.assertEqual(self.solution.findMaxAverage(nums, k), expected)

    def test_findMaxAverage_emptyList(self):
        nums = []
        k = 1
        expected = 0.0
        self.assertEqual(self.solution.findMaxAverage(nums, k), expected)

    def test_findMaxAverage_singleElement(self):
        nums = [10]
        k = 1
        expected = 10.0
        self.assertEqual(self.solution.findMaxAverage(nums, k), expected)


if __name__ == '__main__':
    unittest.main()
