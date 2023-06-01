import unittest
from typing import List

"""

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        zrows, zcols = set(), set()

        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    zrows.add(row)
                    zcols.add(col)

        for row in zrows:
            for col in range(COLS):
                matrix[row][col] = 0

        for col in zcols:
            for row in range(ROWS):
                matrix[row][col] = 0

        # print(zrows, zcols)
        # print(matrix)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_setZeroes(self):
        # Test case 1
        matrix1 = [[1, 1, 1],
                   [1, 0, 1],
                   [1, 1, 1]]
        expected1 = [[1, 0, 1],
                     [0, 0, 0],
                     [1, 0, 1]]
        self.solution.setZeroes(matrix1)
        self.assertEqual(matrix1, expected1)

        # Test case 2
        matrix2 = [[0, 1, 2, 0],
                   [3, 4, 5, 2],
                   [1, 3, 1, 5]]
        expected2 = [[0, 0, 0, 0],
                     [0, 4, 5, 0],
                     [0, 3, 1, 0]]
        self.solution.setZeroes(matrix2)
        self.assertEqual(matrix2, expected2)

        # Test case 3
        matrix3 = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]
        expected3 = [[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]]
        self.solution.setZeroes(matrix3)
        self.assertEqual(matrix3, expected3)

if __name__ == '__main__':
    unittest.main()
