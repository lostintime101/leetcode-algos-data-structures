import unittest
import collections

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

"""


class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:

        # ORIGINAL
        # counterpoints = []

        # for num in nums:

        #     if num in counterpoints:
        #         a = nums.index(num)
        #         b = target-num
        #         nums[a] = -1000000
        #         return [a, nums.index(b)]

        #     counterpoints.append(target - num)

        # HASH MAP
        second = collections.defaultdict(list)

        for i, v in enumerate(nums):

            if target - v in second: return [i, second[target - v]]

            second[v] = i


class TestSolution(unittest.TestCase):

    def test_twoSum(self):
        solution = Solution()

        # Test case 1
        nums1 = [2, 7, 11, 15]
        target1 = 9
        expected_output1 = {0, 1}
        self.assertSetEqual(set(solution.twoSum(nums1, target1)), expected_output1)

        # Test case 2
        nums2 = [3, 2, 4]
        target2 = 6
        expected_output2 = {1, 2}
        self.assertEqual(set(solution.twoSum(nums2, target2)), expected_output2)

        # Test case 3
        nums3 = [3, 3]
        target3 = 6
        expected_output3 = {0, 1}
        self.assertEqual(set(solution.twoSum(nums3, target3)), expected_output3)


if __name__ == '__main__':
    unittest.main()
