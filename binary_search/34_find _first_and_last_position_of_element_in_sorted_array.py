import unittest
from typing import List

"""

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        l, r = 0, len(nums) - 1

        found = False
        while l <= r:

            mid = (l + r) // 2
            if nums[mid] == target:
                found = True
                break
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        if found == False: return [-1, -1]

        left, right = mid, mid

        while (0 < (left)) and nums[left - 1] == target: left -= 1
        while (len(nums) - 1 > right) and nums[right + 1] == target: right += 1

        return [left, right]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 8
        expected_output = [3, 4]
        self.assertEqual(self.solution.searchRange(nums, target), expected_output)

    def test_case_2(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 6
        expected_output = [-1, -1]
        self.assertEqual(self.solution.searchRange(nums, target), expected_output)

    def test_case_3(self):
        nums = [1, 2, 3, 4, 5]
        target = 3
        expected_output = [2, 2]
        self.assertEqual(self.solution.searchRange(nums, target), expected_output)

    def test_case_4(self):
        nums = []
        target = 5
        expected_output = [-1, -1]
        self.assertEqual(self.solution.searchRange(nums, target), expected_output)

    def test_case_5(self):
        nums = [2, 2, 2, 2, 2]
        target = 2
        expected_output = [0, 4]
        self.assertEqual(self.solution.searchRange(nums, target), expected_output)


if __name__ == "__main__":
    unittest.main()
