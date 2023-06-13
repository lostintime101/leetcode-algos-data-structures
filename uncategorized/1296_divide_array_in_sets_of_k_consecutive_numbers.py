import unittest
from typing import List
from collections import Counter

"""

Given an array of integers nums and a positive integer k, 
check whether it is possible to divide this array into sets of k consecutive numbers.

Return true if it is possible. Otherwise, return false.

Constraints:

1 <= k <= nums.length <= 105
1 <= nums[i] <= 109

"""

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:

        freq, total = Counter(nums), len(nums)

        if total % k: return False
        if k == 1: return True

        while total:

            start = min(freq.keys())

            for i in range(k):
                if not freq[start + i]: return False
                freq[start + i] -= 1
                total -= 1
                if freq[start + i] == 0: del freq[start + i]

        return True


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_isPossibleDivide_true(self):
        nums = [1, 2, 3, 4, 5, 6]
        k = 2
        self.assertTrue(self.solution.isPossibleDivide(nums, k))

        nums = [1, 2, 3, 4, 5, 6, 7, 8]
        k = 4
        self.assertTrue(self.solution.isPossibleDivide(nums, k))

        nums = [4, 6, 8, 10, 12, 14]
        k = 2
        self.assertFalse(self.solution.isPossibleDivide(nums, k))

    def test_isPossibleDivide_false(self):
        nums = [1, 2, 3, 4, 5, 6]
        k = 4
        self.assertFalse(self.solution.isPossibleDivide(nums, k))

        nums = [1, 2, 3, 4, 5, 7]
        k = 3
        self.assertFalse(self.solution.isPossibleDivide(nums, k))

        nums = [1, 2, 3, 4, 5, 6, 8]
        k = 2
        self.assertFalse(self.solution.isPossibleDivide(nums, k))

if __name__ == '__main__':
    unittest.main()
