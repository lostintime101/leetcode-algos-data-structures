import unittest
from collections import Counter
from typing import List

"""

You are given a 0-indexed array nums consisting of positive integers.

There are two types of operations that you can apply on the array any number of times:

Choose two elements with equal values and delete them from the array.
Choose three elements with equal values and delete them from the array.
Return the minimum number of operations required to make the array empty, or -1 if it is not possible.

Constraints:

2 <= nums.length <= 105
1 <= nums[i] <= 106

"""

class Solution:
    def minOperations(self, nums: List[int]) -> int:

        ans = 0
        freq = Counter(nums)

        for k, v in freq.items():
            if v == 1: return -1

            curr = v % 3
            ans += v // 3
            if curr == 1 or curr == 2: ans += 1

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_min_operations_valid_input(self):
        nums = [1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
        self.assertEqual(self.solution.minOperations(nums), -1)

    def test_min_operations_single_element(self):
        nums = [5]
        self.assertEqual(self.solution.minOperations(nums), -1)

    def test_min_operations_no_operations_needed(self):
        nums = [3, 3, 3, 6, 6, 6, 9, 9, 9]
        self.assertEqual(self.solution.minOperations(nums), 3)

    def test_min_operations_invalid_input(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.minOperations(nums), -1)

    def test_min_operations_empty_input(self):
        nums = []
        self.assertEqual(self.solution.minOperations(nums), 0)

if __name__ == '__main__':
    unittest.main()
