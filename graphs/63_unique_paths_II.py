import unittest
from typing import List

"""

You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

Constraints:

m == obstacle_grid.length
n == obstacle_grid[i].length
1 <= m, n <= 100
obstacle_grid[i][j] is 0 or 1.


"""


class Solution:
    def uniquePathsWithObstacles(self, obstacle_grid: List[List[int]]) -> int:

        ROWS, COLS = len(obstacle_grid), len(obstacle_grid[0])

        for i in range(ROWS - 1, -1, -1):

            for j in range(COLS - 1, -1, -1):

                if i == ROWS - 1 and j == COLS - 1:
                    if obstacle_grid[i][j] != 1:
                        obstacle_grid[i][j] = 1
                    else:
                        return 0
                    continue

                if obstacle_grid[i][j] == 1:
                    obstacle_grid[i][j] = 0
                    continue

                if j != COLS - 1:
                    obstacle_grid[i][j] += obstacle_grid[i][j + 1]

                if i != ROWS - 1:
                    obstacle_grid[i][j] += obstacle_grid[i + 1][j]

        return obstacle_grid[0][0]


class TestUniquePathsWithObstacles(unittest.TestCase):
    def test_obstacleGrid_with_no_obstacles(self):
        solution = Solution()
        obstacle_grid = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(solution.uniquePathsWithObstacles(obstacle_grid), 6)

    def test_obstacleGrid_with_obstacles(self):
        solution = Solution()
        obstacle_grid = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        self.assertEqual(solution.uniquePathsWithObstacles(obstacle_grid), 2)

    def test_obstacleGrid_with_single_obstacle(self):
        solution = Solution()
        obstacle_grid = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]
        self.assertEqual(solution.uniquePathsWithObstacles(obstacle_grid), 0)

    def test_obstacleGrid_with_large_obstacle(self):
        solution = Solution()
        obstacle_grid = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 1, 0]
        ]
        self.assertEqual(solution.uniquePathsWithObstacles(obstacle_grid), 10)


if __name__ == '__main__':
    unittest.main()
