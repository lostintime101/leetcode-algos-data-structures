import unittest

"""

There are n pieces arranged in a line, and each piece is colored either by 'A' or by 'B'. You are given a string colors of length n where colors[i] is the color of the ith piece.

Alice and Bob are playing a game where they take alternating turns removing pieces from the line. In this game, Alice moves first.

Alice is only allowed to remove a piece colored 'A' if both its neighbors are also colored 'A'. She is not allowed to remove pieces that are colored 'B'.
Bob is only allowed to remove a piece colored 'B' if both its neighbors are also colored 'B'. He is not allowed to remove pieces that are colored 'A'.
Alice and Bob cannot remove pieces from the edge of the line.
If a player cannot make a move on their turn, that player loses and the other player wins.
Assuming Alice and Bob play optimally, return true if Alice wins, or return false if Bob wins.

 Constraints:

1 <= colors.length <= 105
colors consists of only the letters 'A' and 'B'

"""

class Solution:
    def winnerOfGame(self, colors: str) -> bool:

        plays = {"A": 0, "B": 0}
        curr, streak = colors[0], 1

        for i in range(1, len(colors)):

            if colors[i] == curr:
                streak += 1
            else:
                curr = colors[i]
                streak = 1

            if streak > 2: plays[curr] += 1

        return plays["A"] > plays["B"]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_color_should_return_false(self):
        self.assertFalse(self.solution.winnerOfGame("A"))
        self.assertFalse(self.solution.winnerOfGame("B"))

    def test_no_consecutive_colors_should_return_false(self):
        self.assertFalse(self.solution.winnerOfGame("ABABAB"))
        self.assertFalse(self.solution.winnerOfGame("BABABA"))

    def test_consecutive_colors_less_than_3_should_return_false(self):
        self.assertTrue(self.solution.winnerOfGame("AAA"))
        self.assertFalse(self.solution.winnerOfGame("ABA"))
        self.assertFalse(self.solution.winnerOfGame("BAA"))

    def test_consecutive_colors_more_than_2_for_A_should_return_true(self):
        self.assertTrue(self.solution.winnerOfGame("AAAB"))
        self.assertFalse(self.solution.winnerOfGame("AABBBAA"))
        self.assertTrue(self.solution.winnerOfGame("AAABAAAA"))

    def test_consecutive_colors_more_than_2_for_B_should_return_false(self):
        self.assertFalse(self.solution.winnerOfGame("BBB"))
        self.assertTrue(self.solution.winnerOfGame("BABAAA"))
        self.assertTrue(self.solution.winnerOfGame("BBBAAAA"))

if __name__ == "__main__":
    unittest.main()
