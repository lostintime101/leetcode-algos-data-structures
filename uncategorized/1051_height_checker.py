import unittest
from typing import List

"""
A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.

You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

Return the number of indices where heights[i] != expected[i].

Constraints:

1 <= heights.length <= 100
1 <= heights[i] <= 100

"""

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        ans = 0
        N = len(heights)

        for i in range(N):
            if sorted_heights[i] != heights[i]:
                ans += 1

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        heights = [1, 1, 4, 2, 1, 3]
        expected = 3
        result = self.solution.heightChecker(heights)
        self.assertEqual(result, expected)

    def test_case_2(self):
        heights = [5, 1, 2, 3, 4]
        expected = 5
        result = self.solution.heightChecker(heights)
        self.assertEqual(result, expected)

    def test_case_3(self):
        heights = [1, 2, 3, 4, 5]
        expected = 0
        result = self.solution.heightChecker(heights)
        self.assertEqual(result, expected)

    def test_case_4(self):
        heights = [2, 1, 2, 1, 1, 2, 2, 1]
        expected = 4
        result = self.solution.heightChecker(heights)
        self.assertEqual(result, expected)

    def test_case_empty(self):
        heights = []
        expected = 0
        result = self.solution.heightChecker(heights)
        self.assertEqual(result, expected)

    def test_case_single_element(self):
        heights = [1]
        expected = 0
        result = self.solution.heightChecker(heights)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
