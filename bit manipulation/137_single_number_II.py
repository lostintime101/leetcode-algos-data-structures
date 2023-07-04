import unittest
from typing import List

"""

Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Constraints:

1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each element in nums appears exactly three times except for one element which appears once.

"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        tally = [0] * 32

        for i in range(len(nums)):

            a = bin(nums[i])
            if a[0] == "-":
                a = a[3:]
            else:
                a = a[2:]

            a = a[::-1]

            for i in range(len(a)):
                tally[i] += int(a[i])

        for i in range(len(tally)):
            tally[i] %= 3
            tally[i] = str(tally[i])
        tally = int("".join(tally[::-1]), 2)

        # TODO: IMPROVE THE FUDGED SOLUTION TO SOLVE FOR NEGATIVE NUMBERS
        neg_count, pos_count = 0, 0
        for i in range(len(nums)):
            if nums[i] == tally: pos_count += 1
            if nums[i] == tally * -1: neg_count += 1

        if neg_count == 1: return tally * -1
        return tally



class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_single_number_positive(self):
        nums = [2, 2, 3, 2]
        result = self.solution.singleNumber(nums)
        self.assertEqual(result, 3)

    def test_single_number_negative(self):
        nums = [-4, 1, 2, 2, 2, 1, 1]
        result = self.solution.singleNumber(nums)
        self.assertEqual(result, -4)

    def test_single_number_mixed(self):
        nums = [-1, -1, -1, -2, -3, -2, -3, -2, -3, 0]
        result = self.solution.singleNumber(nums)
        self.assertEqual(result, 0)

    def test_single_number_zero(self):
        nums = [0, 1, 0, 1, 0, 1, -2]
        result = self.solution.singleNumber(nums)
        self.assertEqual(result, -2)

    def test_single_number_large(self):
        nums = [1000000000, 1, 1000000000, 1000000000, 999999999, 999999999, 999999999]
        result = self.solution.singleNumber(nums)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
