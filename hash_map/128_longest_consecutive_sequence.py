import unittest
from typing import List

"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109

"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # SORT FUNCTION
        # if len(nums) == 0: return 0

        # ret, curr = 1, 1
        # nums = sorted(nums)

        # for i in range(len(nums)-1):

        #     if nums[i+1] == nums[i] + 1: curr += 1
        #     elif nums[i+1] == nums[i]: continue
        #     else: curr = 1

        #     if curr > ret: ret = curr

        # return ret

        # SET SOLUTION

        numSet = set(nums)
        curr, ret = 0, 0

        for i in range(len(nums)):

            if nums[i] - 1 not in numSet:
                curr = 1
                while nums[i] + curr in numSet: curr += 1
                ret = max(curr, ret)

        return ret


class TestSolution(unittest.TestCase):

    def test_longestConsecutive(self):
        sol = Solution()

        # Test case 1
        nums = [100, 4, 200, 1, 3, 2]
        expected_output = 4
        self.assertEqual(sol.longestConsecutive(nums), expected_output)

        # Test case 2
        nums = [0, 0, -1]
        expected_output = 2
        self.assertEqual(sol.longestConsecutive(nums), expected_output)

        # Test case 3
        nums = [1, 3, 5, 7, 9]
        expected_output = 1
        self.assertEqual(sol.longestConsecutive(nums), expected_output)

        # Test case 4
        nums = []
        expected_output = 0
        self.assertEqual(sol.longestConsecutive(nums), expected_output)

if __name__ == '__main__':
    unittest.main()
