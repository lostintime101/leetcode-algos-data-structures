import unittest
from typing import List

""""

You are given an m x n binary matrix grid.

A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score after making any number of moves (including zero moves).

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
grid[i][j] is either 0 or 1.

"""

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])
        ans = 0

        def flip_col(c):
            for row in range(ROWS):
                if grid[row][c] == 0:
                    grid[row][c] = 1
                else:
                    grid[row][c] = 0

        def flip_row(r):
            for i, v in enumerate(grid[r]):
                if v == 0:
                    grid[r][i] = 1
                else:
                    grid[r][i] = 0

        for row in range(ROWS):
            if grid[row][0] == 0:
                flip_row(row)

        for col in range(1, COLS):
            total = 0
            for row in range(ROWS):
                if grid[row][col] == 1:
                    total += 1

            if total < (ROWS / 2):
                flip_col(col)

        for row in grid:
            n = "0b" + "".join([str(num) for num in row])
            ans += int(n, 2)

        return ans


class TestSolution(unittest.TestCase):
    def test_matrixScore(self):
        solution = Solution()

        # Test case 1
        grid1 = [
            [0, 0, 1, 1],
            [1, 0, 1, 0],
            [1, 1, 0, 0]
        ]
        self.assertEqual(solution.matrixScore(grid1), 39)

        # Test case 2
        grid2 = [
            [0, 1],
            [1, 1],
            [0, 1]
        ]
        self.assertEqual(solution.matrixScore(grid2), 8)

        # Test case 3
        grid3 = [
            [1, 1, 0],
            [1, 0, 1],
            [0, 0, 1]
        ]
        self.assertEqual(solution.matrixScore(grid3), 18)

        # Additional test case
        grid4 = [
            [0, 0],
            [0, 0]
        ]
        self.assertEqual(solution.matrixScore(grid4), 6)


if __name__ == "__main__":
    unittest.main()
