import unittest
from typing import List

"""

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104

"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # BINARY SEARCH
        l, r = 0, len(nums) - 1
        start, end = nums[0], nums[-1]

        # edge case
        if start == target: return 0

        while l <= r:

            mid = (l + r) // 2
            guess = nums[mid]

            if guess == target: return mid

            # first half of array (pre-pivot)
            if guess >= start:

                if (guess > target) and (target > start):
                    r = mid - 1
                elif (guess > target) and (target < start):
                    l = mid + 1
                else:
                    l = mid + 1

            # second half of array (post-pivot)
            if guess < start:

                if (guess < target) and (start < target):
                    r = mid - 1
                elif (guess < target) and (start > target):
                    l = mid + 1
                else:
                    r = mid - 1

        return -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_existing_element_pre_pivot(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 5
        self.assertEqual(self.solution.search(nums, target), 1)

    def test_existing_element_post_pivot(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 1
        self.assertEqual(self.solution.search(nums, target), 5)

    def test_non_existing_element(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        self.assertEqual(self.solution.search(nums, target), -1)

    def test_edge_case(self):
        nums = [1]
        target = 1
        self.assertEqual(self.solution.search(nums, target), 0)

    def test_target_at_pivot(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        self.assertEqual(self.solution.search(nums, target), 4)


if __name__ == '__main__':
    unittest.main()

