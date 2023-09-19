import unittest

"""

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.

"""


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        curr = 0
        nums_set = set()

        for num in nums:
            old_curr = curr
            nums_set.add(num)
            curr = len(nums_set)
            if curr == old_curr: return num


class TestSolution(unittest.TestCase):
    def test_find_duplicate(self):
        solution = Solution()

        # Test case 1: Basic test with duplicate
        nums1 = [1, 3, 4, 2, 2]
        self.assertEqual(solution.findDuplicate(nums1), 2)

        # Test case 2: Duplicate at the beginning
        nums2 = [2, 1, 3, 4, 2]
        self.assertEqual(solution.findDuplicate(nums2), 2)

        # Test case 3: No duplicate
        nums3 = [1, 2, 3, 4, 5]
        self.assertIsNone(solution.findDuplicate(nums3))

        # Test case 4: Duplicate at the end
        nums4 = [1, 3, 4, 2, 5, 5]
        self.assertEqual(solution.findDuplicate(nums4), 5)


if __name__ == '__main__':
    unittest.main()
