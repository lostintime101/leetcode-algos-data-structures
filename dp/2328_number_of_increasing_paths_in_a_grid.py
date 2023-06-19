import unittest
from typing import List
from collections import defaultdict

"""

You are given an m x n integer matrix grid, where you can move from a cell to any adjacent cell in all 4 directions.

Return the number of strictly increasing paths in the grid such that you can start from any cell and end at any cell.
Since the answer may be very large, return it modulo 109 + 7.

Two paths are considered different if they do not have exactly the same sequence of visited cells.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
1 <= grid[i][j] <= 105

"""


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:

        ans = [0]
        ROWS, COLS = len(grid), len(grid[0])
        mapping = defaultdict(list)
        unique_vals = set()
        grid2 = [[0 for i in range(COLS)] for j in range(ROWS)]

        for row in range(ROWS):
            for col in range(COLS):
                mapping[grid[row][col]].append((row, col))
                unique_vals.add(grid[row][col])

        unique_vals = sorted(list(unique_vals))[::-1]

        # checks up,down,left,right for larger ints, marks grid 2
        def check_for_paths(loc: tuple):

            r, c = loc[0], loc[1]
            paths = 0

            if r and (grid[r - 1][c] > grid[r][c]): paths += 1 + grid2[r - 1][c]
            if c and (grid[r][c - 1] > grid[r][c]): paths += 1 + grid2[r][c - 1]
            if r != ROWS - 1 and (grid[r + 1][c] > grid[r][c]): paths += 1 + grid2[r + 1][c]
            if c != COLS - 1 and (grid[r][c + 1] > grid[r][c]): paths += 1 + grid2[r][c + 1]

            grid2[r][c] = paths
            ans[0] += 1 + paths

            return

        for val in unique_vals:
            for location in mapping[val]: check_for_paths(location)

        ans = ans[0] % (10 ** 9 + 7)
        return ans


class SolutionTestCase(unittest.TestCase):

    def test_countPaths(self):
        solution = Solution()

        # Test case 1
        grid1 = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual(solution.countPaths(grid1), 53)

        # Test case 2
        grid2 = [
            [5, 6, 7],
            [4, 5, 8],
            [3, 2, 1]
        ]
        self.assertEqual(solution.countPaths(grid2), 72)

        # Test case 4 (single cell)
        grid4 = [[1]]
        self.assertEqual(solution.countPaths(grid4), 1)

        # Test case 5 (grid with identical values)
        grid5 = [
            [2, 2],
            [2, 2]
        ]
        self.assertEqual(solution.countPaths(grid5), 4)

if __name__ == '__main__':
    unittest.main()
