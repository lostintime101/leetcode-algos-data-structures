import unittest
from typing import List

"""

Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
Each element in nums appears once or twice.

"""

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        N = len(nums)
        ans = []

        for i in range(N):

            curr = nums[i]
            if curr < 0: curr *= -1
            curr -= 1

            if nums[curr] < 0:
                ans.append(curr + 1)
            else:
                nums[curr] = nums[curr] * -1

        return ans


class TestSolution(unittest.TestCase):
    def test_findDuplicates(self):
        solution = Solution()

        # Test case where there are duplicates
        nums1 = [4, 3, 2, 7, 8, 2, 3, 1]
        expected_output1 = [2, 3]
        self.assertEqual(solution.findDuplicates(nums1), expected_output1)

        # Test case where all elements are unique
        nums2 = [1, 2, 3, 4, 5]
        expected_output2 = []
        self.assertEqual(solution.findDuplicates(nums2), expected_output2)

        # Test case where duplicates occur at the beginning and end
        nums5 = [1, 2, 3, 4, 1, 5, 6, 7, 8, 9, 9]
        expected_output5 = [1, 9]
        self.assertEqual(solution.findDuplicates(nums5), expected_output5)


if __name__ == '__main__':
    unittest.main()
