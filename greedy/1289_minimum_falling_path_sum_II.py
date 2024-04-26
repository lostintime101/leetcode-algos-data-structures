import unittest
from math import inf
from typing import List

"""

Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.

A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that no two elements chosen in adjacent rows are in the same column.

Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
-99 <= grid[i][j] <= 99

"""

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])
        new_grid = [[float(inf) for _ in range(COLS)] for _ in range(ROWS)]
        new_grid[0] = grid[0]

        for row in range(1, ROWS):
            for col in range(COLS):

                if col == 0:
                    left = float(inf)
                else:
                    left = min(new_grid[row - 1][:col])

                if col == COLS - 1:
                    right = float(inf)
                else:
                    right = min(new_grid[row - 1][col + 1:])

                new_grid[row][col] = min(left, right) + grid[row][col]

        return min(new_grid[-1])


class TestSolution(unittest.TestCase):
    def test_minFallingPathSum(self):
        solution = Solution()

        # Test case 1: Small grid
        grid1 = [
            [2, 1, 3],
            [6, 5, 4],
            [7, 8, 9]
        ]
        self.assertEqual(solution.minFallingPathSum(grid1), 12)

        # Test case 2: Grid with negative numbers
        grid2 = [
            [1, 2, 3],
            [-6, -5, -4],
            [7, 8, 9]
        ]
        self.assertEqual(solution.minFallingPathSum(grid2), 3)

        # Test case 3: Grid with one row
        grid3 = [
            [1, 2, 3]
        ]
        self.assertEqual(solution.minFallingPathSum(grid3), 1)


if __name__ == '__main__':
    unittest.main()
