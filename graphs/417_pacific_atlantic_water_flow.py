import unittest
from typing import List

"""

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105

"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS, COLS, ret = len(heights), len(heights[0]), []

        pac = [[0 if c != 0 else 1 for c in range(COLS)] if r != 0 else [1 for c in range(COLS)] for r in range(ROWS)]
        atl = [[0 if c != (COLS - 1) else 1 for c in range(COLS)] if r != (ROWS - 1) else [1 for c in range(COLS)] for r
               in range(ROWS)]

        def check(grid, r, c):

            if grid[r][c] == 1: return False

            if (r and (heights[r - 1][c] <= heights[r][c]) and grid[r - 1][c]) or \
                    (c and (heights[r][c - 1] <= heights[r][c]) and grid[r][c - 1]) or \
                    ((r != ROWS - 1) and (heights[r + 1][c] <= heights[r][c]) and grid[r + 1][c]) or \
                    ((c != COLS - 1) and (heights[r][c + 1] <= heights[r][c]) and grid[r][c + 1]):
                grid[r][c] = 1
                return True
            return False

        found = True
        while found:
            found = False
            for row in range(ROWS):
                for col in range(COLS):
                    if check(pac, row, col) or check(atl, row, col): found = True

        for row in range(ROWS):
            for col in range(COLS):
                if atl[row][col] and pac[row][col]:
                    ret.append([row, col])

        return ret


class TestSolution(unittest.TestCase):
    def test_pacificAtlantic(self):
        solution = Solution()

        heights = [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4]
        ]
        expected = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        self.assertEqual(solution.pacificAtlantic(heights), expected)

        heights = [
            [3, 3, 3, 3, 3],
            [3, 0, 3, 0, 3],
            [3, 3, 3, 3, 3]
        ]
        expected = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 2], [1, 4], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4]]
        self.assertEqual(solution.pacificAtlantic(heights), expected)

        heights = [
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5]
        ]
        expected = [[0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
        self.assertEqual(solution.pacificAtlantic(heights), expected)

if __name__ == '__main__':
    unittest.main()

