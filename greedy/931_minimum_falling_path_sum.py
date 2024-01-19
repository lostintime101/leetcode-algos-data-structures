import unittest
from typing import List

"""

Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 100
-100 <= matrix[i][j] <= 100


"""

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        ROWS = len(matrix)
        COLS = len(matrix[0])

        for row in range(1, ROWS):
            for col in range(COLS):

                left, right, center = float("inf"), float("inf"), float("inf")
                center = matrix[row - 1][col]
                if col != 0: left = matrix[row - 1][col - 1]
                if col != COLS - 1: right = matrix[row - 1][col + 1]

                matrix[row][col] += min(left, right, center)

        return min(matrix[-1])


class TestSolution(unittest.TestCase):
    def test_minFallingPathSum(self):
        # Test case 1
        matrix1 = [
            [2, 1, 3],
            [6, 5, 4],
            [7, 8, 9]
        ]
        solution1 = Solution()
        self.assertEqual(solution1.minFallingPathSum(matrix1), 13)

        # Test case 2
        matrix2 = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        solution2 = Solution()
        self.assertEqual(solution2.minFallingPathSum(matrix2), 12)


if __name__ == '__main__':
    unittest.main()
