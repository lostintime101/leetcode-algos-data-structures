import unittest

"""

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

"""


class Solution:
    def numIslands(self, grid: [[str]]) -> int:

        islands = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        def markIsland(row, col):

            if (0 > row) or (row > ROWS - 1) or (0 > col) or (col > COLS - 1): return
            if grid[row][col] != "1": return

            grid[row][col] = "2"

            markIsland(row, col + 1) or markIsland(row, col - 1) or markIsland(row + 1, col) or markIsland(row - 1, col)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    islands += 1
                    markIsland(row, col)

        return islands


class SolutionTests(unittest.TestCase):

    def test_numIslands_returns_zero_when_no_islands_exist(self):
        grid = [
            ['0', '0', '0', '0'],
            ['0', '0', '0', '0'],
            ['0', '0', '0', '0'],
            ['0', '0', '0', '0']
        ]
        solution = Solution()
        self.assertEqual(solution.numIslands(grid), 0)

    def test_numIslands_returns_correct_count_for_single_island(self):
        grid = [
            ['1', '1', '1', '1'],
            ['1', '1', '1', '1'],
            ['1', '1', '1', '1'],
            ['1', '1', '1', '1']
        ]
        solution = Solution()
        self.assertEqual(solution.numIslands(grid), 1)

    def test_numIslands_returns_correct_count_for_multiple_islands(self):
        grid = [
            ['1', '1', '0', '0'],
            ['1', '0', '0', '0'],
            ['0', '0', '1', '1'],
            ['0', '0', '1', '1']
        ]
        solution = Solution()
        self.assertEqual(solution.numIslands(grid), 2)

if __name__ == '__main__':
    unittest.main()
