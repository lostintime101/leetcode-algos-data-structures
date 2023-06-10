import unittest
from typing import List

"""

You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, 
that walk over every non-obstacle square exactly once.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
1 <= m * n <= 20
-1 <= grid[i][j] <= 2
There is exactly one starting cell and one ending cell.

"""

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        ret = [0]
        grid_copy = grid[::]
        ROWS = len(grid)
        COLS = len(grid[0])

        def allSquaresVisited(visited: List[List[int]]) -> bool:
            for row in visited:
                for col in row:
                    if col == 0: return False
            return True

        def backtrack(r: int, c: int, visited: List[List[int]]):

            if grid[r][c] == 2:
                if allSquaresVisited(visited): ret[0] += 1
                return

            if r and (visited[r - 1][c] not in [3, -1]):
                if visited[r - 1][c] != 2: visited[r - 1][c] = 3
                backtrack(r - 1, c, visited[::])
                if visited[r - 1][c] != 2: visited[r - 1][c] = 0
            if c and (visited[r][c - 1] not in [3, -1]):
                if visited[r][c - 1] != 2: visited[r][c - 1] = 3
                backtrack(r, c - 1, visited[::])
                if visited[r][c - 1] != 2: visited[r][c - 1] = 0
            if r != ROWS - 1 and (visited[r + 1][c] not in [3, -1]):
                if visited[r + 1][c] != 2: visited[r + 1][c] = 3
                backtrack(r + 1, c, visited[::])
                if visited[r + 1][c] != 2: visited[r + 1][c] = 0
            if c != COLS - 1 and (visited[r][c + 1] not in [3, -1]):
                if visited[r][c + 1] != 2: visited[r][c + 1] = 3
                backtrack(r, c + 1, visited[::])
                if visited[r][c + 1] != 2: visited[r][c + 1] = 0


        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    grid[row][col] = 3
                    backtrack(row, col, grid_copy)

                    return ret[0]


def test_uniquePathsIII():
    solution = Solution()

    # Test case 1
    grid1 = [
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 2, -1]
    ]
    assert solution.uniquePathsIII(grid1) == 2

    # Test case 2
    grid2 = [
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 2]
    ]
    assert solution.uniquePathsIII(grid2) == 4

    # Test case 3
    grid2 = [
        [0, 1],
        [2, 0]
    ]
    assert solution.uniquePathsIII(grid2) == 0

test_uniquePathsIII()