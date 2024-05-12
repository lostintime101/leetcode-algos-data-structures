from typing import List
import unittest

"""

You are given an n x n integer matrix grid.

Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

Return the generated matrix.

"""

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        N = len(grid)
        ans = [[0 for _ in range(N-2)] for _ in range(N-2)]
        ROWS = len(ans)
        COLS = len(ans[0])


        for row in range(ROWS):
            for col in range(COLS):
                ans[row][col] = max(
                    grid[row][col],
                    grid[row+1][col],
                    grid[row+2][col],
                    grid[row][col+1],
                    grid[row+1][col+1],
                    grid[row+2][col+1],
                    grid[row][col+2],
                    grid[row+1][col+2],
                    grid[row+2][col+2],
                    )

        return ans


class TestSolution(unittest.TestCase):
    def test_largestLocal(self):
        solution = Solution()

        # Test case 1
        grid1 = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected1 = [[9]]
        self.assertEqual(solution.largestLocal(grid1), expected1)

        # Test case 2
        grid2 = [
            [9, 2, 3],
            [4, 8, 6],
            [7, 1, 5]
        ]
        expected2 = [[9]]
        self.assertEqual(solution.largestLocal(grid2), expected2)


if __name__ == '__main__':
    unittest.main()
