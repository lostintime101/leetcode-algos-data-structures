import unittest
from typing import List

"""

You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.

"""

class Solution:
    def specialArray(self, nums: List[int]) -> int:

        nums = sorted(nums, reverse=True)

        N = len(nums)
        if nums[-1] >= N: return N

        for i in range(N - 1):

            if nums[i] >= i + 1 and nums[i + 1] < i + 1:
                return i + 1

        return -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.specialArray([3, 5]), 2)

    def test_example2(self):
        self.assertEqual(self.solution.specialArray([0, 0]), -1)

    def test_example3(self):
        self.assertEqual(self.solution.specialArray([0, 4, 3, 0, 4]), 3)

    def test_example4(self):
        self.assertEqual(self.solution.specialArray([3, 6, 7, 7, 0]), -1)

    def test_single_element(self):
        self.assertEqual(self.solution.specialArray([1]), 1)

    def test_no_special_value(self):
        self.assertEqual(self.solution.specialArray([1, 2, 3, 4, 5, 6]), -1)

    def test_all_zeros(self):
        self.assertEqual(self.solution.specialArray([0, 0, 0, 0]), -1)

    def test_all_equal(self):
        self.assertEqual(self.solution.specialArray([3, 3, 3, 3]), -1)

    def test_large_numbers(self):
        self.assertEqual(self.solution.specialArray([100, 100, 100]), 3)


if __name__ == "__main__":
    unittest.main()
