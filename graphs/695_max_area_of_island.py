import unittest
from typing import List

"""

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 
4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.

"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        max_area, island_area = [0], [0]
        ROWS, COLS = len(grid), len(grid[0])

        def findIslandArea(r, c):

            if grid[r][c] != 1: return

            island_area[0] += 1
            grid[r][c] = 2

            if r: findIslandArea(r - 1, c)
            if c: findIslandArea(r, c - 1)
            if r < ROWS - 1: findIslandArea(r + 1, c)
            if c < COLS - 1: findIslandArea(r, c + 1)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    island_area = [0]
                    findIslandArea(row, col)
                    max_area[0] = max(max_area[0], island_area[0])

        return max_area[0]



class TestSolution(unittest.TestCase):

    def test_maxAreaOfIsland(self):
        solution = Solution()

        # Test case 1
        grid1 = [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]
        ]
        self.assertEqual(solution.maxAreaOfIsland(grid1), 4)

        # Test case 2
        grid2 = [
            [1, 1, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]
        ]
        self.assertEqual(solution.maxAreaOfIsland(grid2), 4)

        # Test case 3
        grid3 = [
            [1, 1, 1],
            [0, 1, 0],
            [1, 1, 1]
        ]
        self.assertEqual(solution.maxAreaOfIsland(grid3), 7)
        

        # Test case 5 (Grid with no islands)
        grid5 = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(solution.maxAreaOfIsland(grid5), 0)

if __name__ == '__main__':
    unittest.main()
