import unittest
import collections

"""

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.

"""

class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:

        # ORIGINAL REFACTORED

        # vert = [[] for n in range(9)]
        # boxes = [[] for n in range(9)]

        # for i,v in enumerate(board):

        #     hori = []

        #     for ii, vv in enumerate(v):

        #         if vv.isnumeric():
        #             box = ((ii // 3)) + ((i // 3)*3)

        #             if (vv in hori) or (vv in vert[ii]) or (vv in boxes[box]):
        #                 return False
        #             else:
        #                 hori.append(vv)
        #                 vert[ii].append(vv)
        #                 boxes[box].append(vv)

        # return True

        # USING DEFAULTDICT HASHMAPS

        hori = collections.defaultdict(set)
        vert = collections.defaultdict(set)
        boxes = collections.defaultdict(set)

        for row in range(9):
            for col in range(9):
                vv = board[row][col]
                if vv not in [",", "."]:
                    box = ((col // 3)) + ((row // 3) * 3)

                    a = len(hori[row])
                    hori[row].add(vv)
                    if len(hori[row]) == a: return False

                    b = len(vert[col])
                    vert[col].add(vv)
                    if len(vert[col]) == b: return False

                    c = len(boxes[box])
                    boxes[box].add(vv)
                    if len(boxes[box]) == c: return False

        return True


class TestIsValidSudoku(unittest.TestCase):
    def test_valid_board(self):
        board = [
            ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
            ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
            ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
            ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
            ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
            ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
            ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
            ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
            ['.', '.', '.', '.', '8', '.', '.', '7', '9']
        ]
        self.assertTrue(Solution().isValidSudoku(board))

    def test_invalid_column(self):
        board = [
            ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
            ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
            ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
            ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
            ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
            ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
            ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
            ['.', '.', '5', '4', '1', '9', '.', '.', '5'],
            ['.', '.', '.', '.', '8', '.', '.', '7', '9']
        ]
        self.assertFalse(Solution().isValidSudoku(board))

    def test_invalid_box(self):
        board = [
            ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
            ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
            ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
            ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
            ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
            ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
            ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
            ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
            ['.', '.', '.', '.', '8', '.', '5', '7', '9']
        ]
        self.assertFalse(Solution().isValidSudoku(board))


if __name__ == '__main__':
    unittest.main()