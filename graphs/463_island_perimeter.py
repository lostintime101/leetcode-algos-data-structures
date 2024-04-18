from typing import List
import unittest

"""

You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
There is exactly one island in grid.

"""

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        ans = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def check_sides(r, c):
            ret = 0
            for (x, y) in dirs:
                dx, dy = r + x, c + y

                if dx == -1 or dy == -1 or dx == ROWS or dy == COLS or grid[dx][dy] == 0:
                    ret += 1

            return ret

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    ans += check_sides(row, col)

        return ans


class TestSolution(unittest.TestCase):
    def test_islandPerimeter(self):
        solution = Solution()

        # Test case 1
        grid1 = [
            [0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]
        ]
        self.assertEqual(solution.islandPerimeter(grid1), 16)

        # Test case 2
        grid2 = [
            [1, 0],
            [1, 1]
        ]
        self.assertEqual(solution.islandPerimeter(grid2), 8)

        # Test case 3
        grid3 = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
        self.assertEqual(solution.islandPerimeter(grid3), 16)


if __name__ == "__main__":
    unittest.main()
