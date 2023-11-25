import unittest
from typing import List

"""

You are given an integer array nums sorted in non-decreasing order.

Build and return an integer array result with the same length as nums such that result[i] is equal to the summation of absolute differences between nums[i] and all the other elements in the array.

In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j < nums.length and j != i (0-indexed).

Constraints:

2 <= nums.length <= 105
1 <= nums[i] <= nums[i + 1] <= 104

"""

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        forward_base = sum(nums)
        backward_base = 0

        for i in range(len(nums)):
            forward = nums[i] * (len(nums) - i) - forward_base
            backward = backward_base - (nums[i] * i)

            backward_base += nums[i]
            forward_base -= nums[i]

            ans[i] = abs(forward + backward)

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_getSumAbsoluteDifferences(self):
        # Test case 1
        nums1 = [2, 3, 5]
        result1 = self.solution.getSumAbsoluteDifferences(nums1)
        self.assertEqual(result1, [4, 3, 5])

        # Test case 2
        nums2 = [1, 4, 6, 8, 10]
        result2 = self.solution.getSumAbsoluteDifferences(nums2)
        self.assertEqual(result2, [24, 15, 13, 15, 21])

        # Add more test cases as needed


if __name__ == "__main__":
    unittest.main()
