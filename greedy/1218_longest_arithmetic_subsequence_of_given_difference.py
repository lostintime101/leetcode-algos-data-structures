from typing import List
from collections import Counter
import unittest

"""

Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.

A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing the order of the remaining elements.

Constraints:

1 <= arr.length <= 105
-104 <= arr[i], difference <= 104

"""


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        ret = 1
        starts = {}

        if difference == 0:
            freq = Counter(arr)
            return max(freq.values())

        for v in arr:

            if v in starts:
                starts[v + difference] = starts[v] + 1
                ret = max(ret, starts[v] + 1)
            else:
                starts[v + difference] = 1

        return ret


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_longestSubsequence_withDifferenceZero(self):
        arr = [1, 2, 3, 3, 3, 4, 5, 5, 5]
        difference = 0
        expected = 3
        result = self.solution.longestSubsequence(arr, difference)
        self.assertEqual(result, expected)

    def test_longestSubsequence_withPositiveDifference(self):
        arr = [1, 5, 7, 9, 13, 15, 17]
        difference = 2
        expected = 3
        result = self.solution.longestSubsequence(arr, difference)
        self.assertEqual(result, expected)

    def test_longestSubsequence_withNegativeDifference(self):
        arr = [5, 3, 1, -1, -3, -5]
        difference = -2
        expected = 6
        result = self.solution.longestSubsequence(arr, difference)
        self.assertEqual(result, expected)

    def test_longestSubsequence_withMixedValues(self):
        arr = [3, 5, 2, 8, 12, 10, 14, 11, 7, 9]
        difference = 2
        expected = 4
        result = self.solution.longestSubsequence(arr, difference)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
