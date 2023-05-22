import unittest

"""

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, 
where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.

"""


class Solution:
    def exist(self, board: [[str]], word: str) -> bool:

        ROWS = len(board)
        COLUMNS = len(board[0])
        found = []

        def backtrack(location, seen, curr):
            curr += 1
            seen.append(location)
            findMatch(location, seen, curr)
            curr -= 1
            seen.pop()
            return (curr, seen)

        def findMatch(location, seen, curr):

            if curr == len(word):
                found.append(1)
                return

            row = location[0]
            column = location[1]

            # ORDER: left, above, right, below
            if column and (board[row][column - 1] == word[curr]) and ([row, column - 1] not in seen):
                curr, seen = backtrack([row, column - 1], seen, curr)

            if row and (board[row - 1][column] == word[curr]) and ([row - 1, column] not in seen):
                curr, seen = backtrack([row - 1, column], seen, curr)

            if (column + 1 != COLUMNS) and (board[row][column + 1] == word[curr]) and ([row, column + 1] not in seen):
                curr, seen = backtrack([row, column + 1], seen, curr)

            if (row + 1 != ROWS) and (board[row + 1][column] == word[curr]) and ([row + 1, column] not in seen):
                curr, seen = backtrack([row + 1, column], seen, curr)

        for row in range(ROWS):

            for column in range(COLUMNS):

                if board[row][column] == word[0]:

                    findMatch([row, column], [[row, column]], 1)
                    if found != []: return True

        return False


class SolutionTests(unittest.TestCase):

    def test_exist_returns_true_when_word_exists(self):
        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        word = "ABCCED"
        solution = Solution()
        self.assertTrue(solution.exist(board, word))

    def test_exist_returns_true_when_word_exists_in_different_order(self):
        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        word = "SEE"
        solution = Solution()
        self.assertTrue(solution.exist(board, word))

    def test_exist_returns_false_when_word_does_not_exist(self):
        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        word = "ABCB"
        solution = Solution()
        self.assertFalse(solution.exist(board, word))


if __name__ == '__main__':
    unittest.main()
