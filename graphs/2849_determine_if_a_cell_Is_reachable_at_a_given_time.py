import unittest

"""

You are given four integers sx, sy, fx, fy, and a non-negative integer t.

In an infinite 2D grid, you start at the cell (sx, sy). Each second, you must move to any of its adjacent cells.

Return true if you can reach cell (fx, fy) after exactly t seconds, or false otherwise.

A cell's adjacent cells are the 8 cells around it that share at least one corner with it. You can visit the same cell several times.

Constraints:

1 <= sx, sy, fx, fy <= 109
0 <= t <= 109

"""


class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:

        limit = max(abs(sx-fx), abs(sy-fy))
        return t >= limit and not (t == 1 and limit == 0)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_reachable_in_time(self):
        self.assertTrue(self.solution.isReachableAtTime(0, 0, 3, 4, 5))

    def test_not_reachable_in_time(self):
        self.assertTrue(self.solution.isReachableAtTime(0, 0, 3, 4, 4))

    def test_reachable_in_exact_time(self):
        self.assertTrue(self.solution.isReachableAtTime(1, 1, 1, 1, 0))

    def test_reachable_with_zero_distance(self):
        self.assertTrue(self.solution.isReachableAtTime(2, 2, 2, 2, 0))

    def test_reachable_with_one_time_unit(self):
        self.assertTrue(self.solution.isReachableAtTime(0, 0, 1, 1, 1))

    def test_not_reachable_with_one_time_unit(self):
        self.assertFalse(self.solution.isReachableAtTime(0, 0, 1, 1, 0))

    def test_negative_coordinates(self):
        self.assertTrue(self.solution.isReachableAtTime(-2, -2, 2, 2, 5))

    def test_large_coordinates(self):
        self.assertTrue(self.solution.isReachableAtTime(10**9, 10**9, 10**9 + 1, 10**9 + 1, 2))


if __name__ == "__main__":
    unittest.main()
