import unittest
from typing import List

"""

You are given a 0-indexed array nums consisting of positive integers.

You can do the following operation on the array any number of times:

Choose an integer i such that 0 <= i < nums.length - 1 and nums[i] <= nums[i + 1]. Replace the element nums[i + 1] with nums[i] + nums[i + 1] and delete the element nums[i] from the array.
Return the value of the largest element that you can possibly obtain in the final array.

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106

"""


class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        ans = 0
        nums = nums[::-1]
        curr = nums[0]
        for i in range(len(nums)-1):
            if curr >= nums[i+1]:
                curr += nums[i+1]
            else:
                curr = nums[i+1]
            ans = max(ans, curr)
        return ans

class TestSolution(unittest.TestCase):

    def test_maxArrayValue_single_element(self):
        sol = Solution()
        nums = [10]
        expected_result = 10
        result = sol.maxArrayValue(nums)
        self.assertEqual(result, expected_result)

    def test_maxArrayValue_positive_numbers(self):
        sol = Solution()
        nums = [2, 3, 7, 1, 4, 6]
        expected_result = 23  # The subarray with the maximum sum is [2, 3, 7, 1], which sums to 13.
        result = sol.maxArrayValue(nums)
        self.assertEqual(result, expected_result)

    def test_maxArrayValue_negative_numbers(self):
        sol = Solution()
        nums = [-2, -3, -1, -5, -4]
        expected_result = 0  # The subarray with the maximum sum is [-1], which sums to -1.
        result = sol.maxArrayValue(nums)
        self.assertEqual(result, expected_result)

    def test_maxArrayValue_mixed_numbers(self):
        sol = Solution()
        nums = [-2, 5, -3, 2, -1, 3, -5, 4]
        expected_result = 5  # The subarray with the maximum sum is [5, -3, 2, -1, 3], which sums to 7.
        result = sol.maxArrayValue(nums)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
