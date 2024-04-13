import unittest
from typing import List
from collections import defaultdict

"""
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Constraints:

rows == matrix.length
cols == matrix[i].length
1 <= row, cols <= 200
matrix[i][j] is '0' or '1'.

"""

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        ROWS = len(matrix)
        COLS = len(matrix[0])

        for row in range(ROWS):
            for col in range(COLS):

                if matrix[row][col] == "1":
                    matrix[row][col] = 1
                else:
                    matrix[row][col] = 0

                if col != 0 and matrix[row][col] != 0 and matrix[row][col - 1] != 0:
                    matrix[row][col] += matrix[row][col - 1]

        ans = 0

        for col in range(COLS):
            possible = defaultdict(int)
            prev = 0
            for row in range(ROWS):

                curr = matrix[row][col]

                for i in range(curr):
                    possible[i + 1] += 1
                    ans = max(ans, possible[i + 1] * (i + 1))

                if prev > curr:
                    for i in range(curr + 1, prev + 1):
                        possible[i] = 0

                prev = curr

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maximalRectangle_1(self):
        matrix = [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]
        ]
        self.assertEqual(self.solution.maximalRectangle(matrix), 6)

    def test_maximalRectangle_2(self):
        matrix = [
            ["0", "1"],
            ["1", "0"]
        ]
        self.assertEqual(self.solution.maximalRectangle(matrix), 1)

    def test_maximalRectangle_3(self):
        matrix = [
            ["0"]
        ]
        self.assertEqual(self.solution.maximalRectangle(matrix), 0)


if __name__ == '__main__':
    unittest.main()
