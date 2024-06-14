import unittest
from typing import List

"""

You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.

Return the minimum number of moves to make every value in nums unique.

The test cases are generated so that the answer fits in a 32-bit integer.

"""

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:

        N = len(nums)
        nums = sorted(nums)
        ans = 0

        for i in range(1, N):

            if nums[i] <= nums[i - 1]:
                ans += (nums[i - 1] + 1 - nums[i])
                nums[i] = nums[i - 1] + 1

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case_1(self):
        self.assertEqual(self.solution.minIncrementForUnique([1, 2, 2]), 1)

    def test_example_case_2(self):
        self.assertEqual(self.solution.minIncrementForUnique([3, 2, 1, 2, 1, 7]), 6)

    def test_all_unique(self):
        self.assertEqual(self.solution.minIncrementForUnique([1, 2, 3, 4, 5]), 0)

    def test_empty_list(self):
        self.assertEqual(self.solution.minIncrementForUnique([]), 0)

    def test_single_element(self):
        self.assertEqual(self.solution.minIncrementForUnique([1]), 0)

    def test_large_identical_elements(self):
        self.assertEqual(self.solution.minIncrementForUnique([5, 5, 5, 5, 5]), 10)

    def test_mixed_case(self):
        self.assertEqual(self.solution.minIncrementForUnique([4, 3, 4, 3, 2]), 4)


if __name__ == '__main__':
    unittest.main()
