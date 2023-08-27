import unittest

"""

You are given a string moves of length n consisting only of characters 'L', 'R', and '_'. The string represents your movement on a number line starting from the origin 0.

In the ith move, you can choose one of the following directions:

move to the left if moves[i] = 'L' or moves[i] = '_'
move to the right if moves[i] = 'R' or moves[i] = '_'
Return the distance from the origin of the furthest point you can get to after n moves.

"""


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:

        position, spaces = 0, 0
        moves = [move for move in moves]

        for move in moves:
            if move == "L":
                position -= 1
            elif move == "R":
                position += 1
            else:
                spaces += 1

        if position < 0:
            return abs(position - spaces)
        else:
            return abs(position + spaces)


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        moves = "LR"
        self.assertEqual(self.solution.furthestDistanceFromOrigin(moves), 0)

    def test_case_2(self):
        moves = "LLLRRR"
        self.assertEqual(self.solution.furthestDistanceFromOrigin(moves), 0)

    def test_case_3(self):
        moves = "LRLLRRLLRRR"
        self.assertEqual(self.solution.furthestDistanceFromOrigin(moves), 1)

    def test_case_4(self):
        moves = "RRLR"
        self.assertEqual(self.solution.furthestDistanceFromOrigin(moves), 2)

    def test_case_5(self):
        moves = "R" * 1000 + "L" * 500
        self.assertEqual(self.solution.furthestDistanceFromOrigin(moves), 500)

    def test_case_6(self):
        moves = "L" * 1000 + "R" * 500
        self.assertEqual(self.solution.furthestDistanceFromOrigin(moves), 500)


if __name__ == '__main__':
    unittest.main()
