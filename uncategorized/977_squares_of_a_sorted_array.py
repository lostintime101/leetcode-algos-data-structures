import unittest
from heapq import heappush, heappop
from typing import List

"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.

"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        heap = []
        for num in nums: heappush(heap, num * num)
        ans = []
        while heap: ans.append(heappop(heap))
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_sortedSquares_emptyList(self):
        result = self.solution.sortedSquares([])
        self.assertEqual(result, [])

    def test_sortedSquares_singleElement(self):
        result = self.solution.sortedSquares([2])
        self.assertEqual(result, [4])

    def test_sortedSquares_positiveNumbers(self):
        result = self.solution.sortedSquares([1, 2, 3, 4])
        self.assertEqual(result, [1, 4, 9, 16])

    def test_sortedSquares_negativeNumbers(self):
        result = self.solution.sortedSquares([-4, -2, 0, 2, 4])
        self.assertEqual(result, [0, 4, 4, 16, 16])

    def test_sortedSquares_mixedNumbers(self):
        result = self.solution.sortedSquares([-3, -2, -1, 0, 2, 5])
        self.assertEqual(result, [0, 1, 4, 4, 9, 25])


if __name__ == '__main__':
    unittest.main()
