import unittest
from typing import List

"""

You are given a 0-indexed m x n binary matrix land where a 0 represents a hectare of forested land and a 1 represents a hectare of farmland.

To keep the land organized, there are designated rectangular areas of hectares that consist entirely of farmland. These rectangular areas are called groups. No two groups are adjacent, meaning farmland in one group is not four-directionally adjacent to another farmland in a different group.

land can be represented by a coordinate system where the top left corner of land is (0, 0) and the bottom right corner of land is (m-1, n-1). Find the coordinates of the top left and bottom right corner of each group of farmland. A group of farmland with a top left corner at (r1, c1) and a bottom right corner at (r2, c2) is represented by the 4-length array [r1, c1, r2, c2].

Return a 2D array containing the 4-length arrays described above for each group of farmland in land. If there are no groups of farmland, return an empty array. You may return the answer in any order.

Constraints:

m == land.length
n == land[i].length
1 <= m, n <= 300
land consists of only 0's and 1's.
Groups of farmland are rectangular in shape.

"""

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:

        ans = []
        ROWS, COLS = len(land), len(land[0])
        DIRS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def check(r, c):

            prev = [[r, c]]
            curr = []
            end = [r, c]

            while prev:
                for [r, c] in prev:
                    for [x, y] in DIRS:
                        [dx, dy] = [r + x, c + y]
                        if dx < 0 or dy < 0 or dx >= ROWS or dy >= COLS:
                            continue
                        if land[dx][dy] == 1:
                            land[dx][dy] = -1
                            curr.append([dx, dy])
                            end = max(end, [dx, dy])

                prev = curr
                curr = []

            return end

        for row in range(ROWS):
            for col in range(COLS):
                if land[row][col] == 1:
                    start = [row, col]
                    land[row][col] = -1
                    end = check(row, col)
                    start.extend(end)
                    ans.append(start)

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_findFarmland_basic(self):
        # Test with a simple case where there's only one plot of land
        land = [[1, 1, 0, 0],
                [1, 1, 0, 1],
                [0, 0, 0, 1]]
        expected = [[0, 0, 1, 1], [1, 3, 2, 3]]
        self.assertEqual(self.solution.findFarmland(land), expected)

    def test_findFarmland_multiple_plots(self):
        # Test with multiple plots of land
        land = [[1, 1, 0, 0],
                [1, 1, 0, 0],
                [0, 0, 1, 1]]
        expected = [[0, 0, 1, 1], [2, 2, 2, 3]]
        self.assertEqual(self.solution.findFarmland(land), expected)

    def test_findFarmland_no_land(self):
        # Test with no land available
        land = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
        expected = []
        self.assertEqual(self.solution.findFarmland(land), expected)

    def test_findFarmland_single_cell(self):
        # Test with only one cell of land
        land = [[1]]
        expected = [[0, 0, 0, 0]]
        self.assertEqual(self.solution.findFarmland(land), expected)

    def test_findFarmland_empty_land(self):
        # Test with an empty land
        land = [[]]
        expected = []
        self.assertEqual(self.solution.findFarmland(land), expected)


if __name__ == '__main__':
    unittest.main()
