import unittest
from typing import List

"""

Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104

"""

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:

        maxi = nums[-1]
        curr_max = 0
        for i in range(len(nums) - 2, -1, -1):

            l = i + 1
            r = min(l + k, len(nums))

            if not curr_max:
                curr_max = max(nums[l:r])
            elif nums[l] > curr_max:
                curr_max = nums[l]
            elif (r < len(nums)) and curr_max == nums[r]:
                curr_max = max(nums[l:r])

            nums[i] = max(nums[i], nums[i] + curr_max)

            maxi = max(maxi, nums[i])

        return maxi


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_constrainedSubsetSum(self):
        # Test Case 1
        nums1 = [10, 2, -10, 5, 20]
        k1 = 2
        self.assertEqual(self.solution.constrainedSubsetSum(nums1, k1), 37)

        # Test Case 2
        nums2 = [-1, -2, -3]
        k2 = 1
        self.assertEqual(self.solution.constrainedSubsetSum(nums2, k2), -1)

        # Test Case 3
        nums3 = [10, -2, 3]
        k3 = 1
        self.assertEqual(self.solution.constrainedSubsetSum(nums3, k3), 11)

        # Additional Test Case
        nums4 = [-1, -1, -1]
        k4 = 2
        self.assertEqual(self.solution.constrainedSubsetSum(nums4, k4), -1)


if __name__ == '__main__':
    unittest.main()

