from collections import Counter
from typing import List
import unittest

"""
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

Constraints:

1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length

"""

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        freq = Counter(arr)
        counts = [val for val in freq.values()]
        counts.sort()

        remove = 0

        for count in counts:

            if count <= k:
                k -= count
                remove += 1
            else:
                break

        return len(counts) - remove


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_findLeastNumOfUniqueInts_case1(self):
        arr = [4, 3, 1, 1, 3, 3, 2, 4, 4]
        k = 3
        result = self.solution.findLeastNumOfUniqueInts(arr, k)
        self.assertEqual(result, 2)

    def test_findLeastNumOfUniqueInts_case2(self):
        arr = [1, 2, 3, 1, 2, 3, 1, 2, 3]
        k = 3
        result = self.solution.findLeastNumOfUniqueInts(arr, k)
        self.assertEqual(result, 2)

    def test_findLeastNumOfUniqueInts_case3(self):
        arr = [1, 1, 1, 2, 2, 2, 3, 3, 3]
        k = 3
        result = self.solution.findLeastNumOfUniqueInts(arr, k)
        self.assertEqual(result, 2)

    def test_findLeastNumOfUniqueInts_case4(self):
        arr = [4, 3, 1, 5, 3, 7, 2, 4, 4]
        k = 5
        result = self.solution.findLeastNumOfUniqueInts(arr, k)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
