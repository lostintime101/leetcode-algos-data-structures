import unittest
from typing import List, Set, Tuple

"""

Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.

"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        ROWS, COLS = len(board), len(board[0])
        seen = set()

        def findAllPointsInRegion(r: int, c: int):
            if board[r][c] != "O": return
            seen.add((r, c))
            board[r][c] = "2"

            if r: findAllPointsInRegion(r - 1, c)
            if c: findAllPointsInRegion(r, c - 1)
            if r < ROWS - 1: findAllPointsInRegion(r + 1, c)
            if c < COLS - 1: findAllPointsInRegion(r, c + 1)

        def shouldFlip(points: Set[Tuple[int, int]]):
            for point in points:
                if point[0] == 0 or point[0] == ROWS - 1 or point[1] == 0 or point[1] == COLS - 1:
                    return False
            return True

        def flip(island: Set[Tuple[int, int]]):
            for coord in island: board[coord[0]][coord[1]] = "X"
            return

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O":
                    findAllPointsInRegion(row, col)
                    if shouldFlip(seen): flip(seen)
                    seen = set()

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "2": board[row][col] = "O"



class TestSolution(unittest.TestCase):

    def test_solve(self):
        solution = Solution()

        # Test case 1
        board1 = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"]
        ]
        expected_board1 = [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "O", "X", "X"]
        ]
        solution.solve(board1)
        self.assertEqual(board1, expected_board1)

        # Test case 2
        board2 = [
            ["O", "O", "O"],
            ["O", "O", "O"],
            ["O", "O", "O"]
        ]
        expected_board2 = [
            ["O", "O", "O"],
            ["O", "O", "O"],
            ["O", "O", "O"]
        ]
        solution.solve(board2)
        self.assertEqual(board2, expected_board2)

        # Test case 3
        board3 = [
            ["X", "X", "X", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
            ["X", "X", "X", "X"]
        ]
        expected_board3 = [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"]
        ]
        solution.solve(board3)
        self.assertEqual(board3, expected_board3)


        # Test case 5 (Board with no 'O' cells)
        board5 = [
            ["X", "X", "X"],
            ["X", "X", "X"],
            ["X", "X", "X"]
        ]
        expected_board5 = [
            ["X", "X", "X"],
            ["X", "X", "X"],
            ["X", "X", "X"]
        ]
        solution.solve(board5)
        self.assertEqual(board5, expected_board5)

if __name__ == '__main__':
    unittest.main()

