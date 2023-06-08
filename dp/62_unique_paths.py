import unittest

"""

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Constraints:

1 <= m, n <= 100

"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        prev = [1 for num in range(n)]
        curr = prev

        for i in range(m - 1):
            for j in range(1, n):
                curr[j] = prev[j] + curr[j - 1]
            prev = curr

        return curr[-1]

        # PREVIOUS SOLUTION
        # m -> rows
        # n -> columns

        # grid = []

        # for row in range(m):

        #     grid.append([0 for i in range(n)])

        #     for column in range(n):

        #         if row == 0:
        #             grid[row][column] = 1

        #         elif column == 0:
        #             grid[row][column] = 1

        #         else:
        #             grid[row][column] = grid[row-1][column] + grid[row][column-1]

        # return grid[-1][-1]



class SolutionTests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_uniquePaths_example1(self):
        result = self.solution.uniquePaths(3, 7)
        self.assertEqual(result, 28)

    def test_uniquePaths_example2(self):
        result = self.solution.uniquePaths(3, 2)
        self.assertEqual(result, 3)

    def test_uniquePaths_example3(self):
        result = self.solution.uniquePaths(7, 3)
        self.assertEqual(result, 28)

    def test_uniquePaths_oneRow(self):
        result = self.solution.uniquePaths(1, 10)
        self.assertEqual(result, 1)

    def test_uniquePaths_oneColumn(self):
        result = self.solution.uniquePaths(10, 1)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
