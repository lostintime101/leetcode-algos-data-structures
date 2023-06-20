import unittest
from typing import List

"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.

"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        time, oranges = -1, set()
        ROWS, COLS = len(grid), len(grid[0])

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    oranges.add((row, col))

        def turn_rotten():
            remove = []
            for orange in oranges:

                r, c = orange[0], orange[1]

                if (r and (grid[r - 1][c] == 2)) or (c and (grid[r][c - 1] == 2)) \
                        or (r != ROWS - 1 and (grid[r + 1][c] == 2)) or (c != COLS - 1 and (grid[r][c + 1] == 2)):
                    remove.append(orange)

            for o in remove:
                grid[o[0]][o[1]] = 2
                oranges.remove(o)

        while oranges:
            time += 1
            before_num = len(oranges)
            turn_rotten()
            after_num = len(oranges)
            if before_num == after_num: break

        if oranges: return -1
        return time + 1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_orangesRotting(self):
        # Test case with no fresh oranges
        grid1 = [[2, 2, 2],
                 [2, 2, 2],
                 [2, 2, 2]]
        self.assertEqual(self.solution.orangesRotting(grid1), 0)

        # Test case with no rotten oranges
        grid2 = [[1, 1, 1],
                 [1, 1, 1],
                 [1, 1, 1]]
        self.assertEqual(self.solution.orangesRotting(grid2), -1)

        # Test case with all fresh oranges
        grid3 = [[1, 1, 1],
                 [1, 1, 1],
                 [1, 1, 1]]
        self.assertEqual(self.solution.orangesRotting(grid3), -1)

        # Test case with mixed fresh and rotten oranges
        grid4 = [[2, 1, 1],
                 [1, 1, 0],
                 [0, 1, 1]]
        self.assertEqual(self.solution.orangesRotting(grid4), 4)

        # Test case with multiple rounds of rotting
        grid5 = [[2, 1, 1],
                 [0, 1, 1],
                 [1, 0, 1]]
        self.assertEqual(self.solution.orangesRotting(grid5), -1)

if __name__ == '__main__':
    unittest.main()
