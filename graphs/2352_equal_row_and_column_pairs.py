import unittest
from typing import List
from collections import defaultdict

"""

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 105

"""

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        # DEFAULTDICT VERSION

        ret = 0
        rows = defaultdict(int)

        for row in grid:
            rows[tuple(row)] += 1

        for col in zip(*grid):
            ret += rows[tuple(col)]

        return ret

        # ORIGINAL TRANSPOSE VERSION

        # ret = 0
        # rows, cols = {}, {}

        # for row in grid:
        #     row = str(row)
        #     if row in rows: rows[row] += 1
        #     else: rows[row] = 1

        # # TODO: transpose grid
        # grid = list(zip(*grid))

        # for col in grid:
        #     col = str(list(col))
        #     if col in rows: ret += rows[col]

        # return ret


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_equalPairs(self):
        grid = [[1, 2], [2, 1]]
        expected = 2
        self.assertEqual(self.solution.equalPairs(grid), expected)

        grid = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        expected = 0
        self.assertEqual(self.solution.equalPairs(grid), expected)

        grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        expected = 9
        self.assertEqual(self.solution.equalPairs(grid), expected)

        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = 0
        self.assertEqual(self.solution.equalPairs(grid), expected)

        grid = [[1, 1, 1], [1, 2, 1], [1, 1, 1]]
        expected = 5
        self.assertEqual(self.solution.equalPairs(grid), expected)

if __name__ == '__main__':
    unittest.main()
