import unittest
from functools import cache
from collections import defaultdict

"""

On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves. The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).

A chess knight has eight possible moves it can make, as illustrated below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.

Constraints:

1 <= n <= 25
0 <= k <= 100
0 <= row, column <= n - 1

"""

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        @cache
        def calculate_valid_moves(start: tuple):

            x, y = start[0], start[1]
            valid_moves = []

            if (x - 2 >= 0) and (y - 1 >= 0): valid_moves.append([x - 2, y - 1])
            if (x - 1 >= 0) and (y - 2 >= 0): valid_moves.append([x - 1, y - 2])
            if (x - 2 >= 0) and (y + 1 <= n - 1): valid_moves.append([x - 2, y + 1])
            if (x - 1 >= 0) and (y + 2 <= n - 1): valid_moves.append([x - 1, y + 2])
            if (x + 1 <= n - 1) and (y - 2 >= 0): valid_moves.append([x + 1, y - 2])
            if (x + 2 <= n - 1) and (y - 1 >= 0): valid_moves.append([x + 2, y - 1])
            if (x + 1 <= n - 1) and (y + 2 <= n - 1): valid_moves.append([x + 1, y + 2])
            if (x + 2 <= n - 1) and (y + 1 <= n - 1): valid_moves.append([x + 2, y + 1])

            return valid_moves

        curr_positions = defaultdict(int)
        curr_positions[tuple([row, column])] = 1

        count = k
        while count:
            new_positions = defaultdict(int)

            for key, val in curr_positions.items():

                moves = calculate_valid_moves(tuple(key))

                for move in moves: new_positions[tuple(move)] += val

            curr_positions = new_positions
            count -= 1

        return (0.125 ** k) * sum(curr_positions.values())



class TestKnightProbability(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_knightProbability_1(self):
        n = 3
        k = 2
        row = 0
        column = 0
        expected_result = 0.0625
        actual_result = self.solution.knightProbability(n, k, row, column)
        self.assertAlmostEqual(expected_result, actual_result, places=5)

    def test_knightProbability_2(self):
        n = 5
        k = 3
        row = 2
        column = 2
        expected_result = 0.25
        actual_result = self.solution.knightProbability(n, k, row, column)
        self.assertAlmostEqual(expected_result, actual_result, places=5)

    def test_knightProbability_3(self):
        n = 4
        k = 1
        row = 3
        column = 3
        expected_result = 0.25
        actual_result = self.solution.knightProbability(n, k, row, column)
        self.assertAlmostEqual(expected_result, actual_result, places=5)

    def test_knightProbability_4(self):
        n = 5
        k = 0
        row = 0
        column = 0
        expected_result = 1.0
        actual_result = self.solution.knightProbability(n, k, row, column)
        self.assertAlmostEqual(expected_result, actual_result, places=5)

    def test_knightProbability_5(self):
        n = 8
        k = 5
        row = 4
        column = 4
        expected_result = 0.35565185546875
        actual_result = self.solution.knightProbability(n, k, row, column)
        self.assertAlmostEqual(expected_result, actual_result, places=5)

if __name__ == '__main__':
    unittest.main()
