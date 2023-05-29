import unittest
from typing import List

"""

You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed. 
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two 
adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000

"""

class Solution:
    def rob(self, nums: List[int]) -> int:

        # DP

        if len(nums) == 1: return nums[0]
        nums1 = nums[1:]
        nums2 = nums[:-1]

        def findMax(array):

            prev, curr = 0, 0
            for i in range(len(array)):
                temp = curr
                curr = max(prev + array[i], curr)
                prev = temp

            return curr

        return max(findMax(nums1), findMax(nums2))



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_rob_example1(self):
        nums = [2, 3, 2]
        result = self.solution.rob(nums)
        self.assertEqual(result, 3)

    def test_rob_example2(self):
        nums = [1, 2, 3, 1]
        result = self.solution.rob(nums)
        self.assertEqual(result, 4)

    def test_rob_example3(self):
        nums = [0]
        result = self.solution.rob(nums)
        self.assertEqual(result, 0)

    def test_rob_custom1(self):
        nums = [1, 2, 3, 4, 5]
        result = self.solution.rob(nums)
        self.assertEqual(result, 8)

    def test_rob_custom2(self):
        nums = [5, 1, 2, 3, 4]
        result = self.solution.rob(nums)
        self.assertEqual(result, 8)

    def test_rob_custom3(self):
        nums = [1, 2, 3, 4, 5, 6]
        result = self.solution.rob(nums)
        self.assertEqual(result, 12)

if __name__ == '__main__':
    unittest.main()
