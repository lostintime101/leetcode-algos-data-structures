import unittest
from typing import List

"""

You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them 
is that adjacent houses have security systems connected 
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400

"""

class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1: return nums[0]
        curr, prev = 0, 0

        # [prev, curr, i, i+1, ...]
        for i in range(len(nums)):
            temp = max(nums[i] + prev, curr)
            prev = curr
            curr = temp

        return curr

        # max1, max2 = 0, 0

        # for i in range(len(nums)):

        #     max1 = max(max1 + nums[i], max2)
        #     max2, max1 = max1, max2

        # return max2


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_rob_example1(self):
        nums = [1, 2, 3, 1]
        result = self.solution.rob(nums)
        self.assertEqual(result, 4)

    def test_rob_example2(self):
        nums = [2, 7, 9, 3, 1]
        result = self.solution.rob(nums)
        self.assertEqual(result, 12)

    def test_rob_custom1(self):
        nums = [5, 3, 2, 6, 1, 4]
        result = self.solution.rob(nums)
        self.assertEqual(result, 15)

    def test_rob_custom2(self):
        nums = [10, 1, 2, 3, 1, 10]
        result = self.solution.rob(nums)
        self.assertEqual(result, 23)

    def test_rob_custom3(self):
        nums = [1, 2, 3, 4, 5, 6]
        result = self.solution.rob(nums)
        self.assertEqual(result, 12)

if __name__ == '__main__':
    unittest.main()
