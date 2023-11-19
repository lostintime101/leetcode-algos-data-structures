import unittest
from typing import List

"""

Given an integer array nums, your goal is to make all elements in nums equal. To complete one operation, follow these steps:

Find the largest value in nums. Let its index be i (0-indexed) and its value be largest. If there are multiple elements with the largest value, pick the smallest i.
Find the next largest value in nums strictly smaller than largest. Let its value be nextLargest.
Reduce nums[i] to nextLargest.
Return the number of operations to make all elements in nums equal.

Constraints:

1 <= nums.length <= 5 * 104
1 <= nums[i] <= 5 * 104

"""

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:

        nums = sorted(nums, reverse=True)

        ans = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]: ans += i

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_reduction_operations_1(self):
        nums = [5, 1, 5]
        result = self.solution.reductionOperations(nums)
        self.assertEqual(result, 2)

    def test_reduction_operations_2(self):
        nums = [1, 1, 2, 2, 3]
        result = self.solution.reductionOperations(nums)
        self.assertEqual(result, 4)

    def test_reduction_operations_3(self):
        nums = [3, 3, 3, 3, 3]
        result = self.solution.reductionOperations(nums)
        self.assertEqual(result, 0)

    def test_reduction_operations_4(self):
        nums = [7, 6, 5, 4, 3, 2, 1]
        result = self.solution.reductionOperations(nums)
        self.assertEqual(result, 21)


if __name__ == '__main__':
    unittest.main()
