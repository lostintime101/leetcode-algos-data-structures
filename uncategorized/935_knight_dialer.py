import unittest

"""

The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L). The possible movements of chess knight are shown in this diagaram:

A chess knight can move as indicated in the chess diagram below:


We have a chess knight and a phone pad as shown below, the knight can only stand on a numeric cell (i.e. blue cell).


Given an integer n, return how many distinct phone numbers of length n we can dial.

You are allowed to place the knight on any numeric cell initially and then you should perform n - 1 jumps to dial a number of length n. All jumps should be valid knight jumps.

As the answer may be very large, return the answer modulo 109 + 7.

Constraints:

1 <= n <= 5000

"""

class Solution:
    def knightDialer(self, n: int) -> int:

        MOD = 10 ** 9 + 7

        nextMoves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }

        prev = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        curr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for _ in range(n - 1):
            for i, v in enumerate(prev):
                for val in nextMoves[i]:
                    curr[val] += prev[i]

            prev = curr
            curr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        return sum(prev) % MOD


class TestKnightDialer(unittest.TestCase):

    def test_knight_dialer_1(self):
        sol = Solution()
        result = sol.knightDialer(1)
        self.assertEqual(result, 10)

    def test_knight_dialer_2(self):
        sol = Solution()
        result = sol.knightDialer(2)
        self.assertEqual(result, 20)

    def test_knight_dialer_3(self):
        sol = Solution()
        result = sol.knightDialer(3)
        self.assertEqual(result, 46)

    def test_knight_dialer_4(self):
        sol = Solution()
        result = sol.knightDialer(4)
        self.assertEqual(result, 104)

    # Add more tests as needed


if __name__ == '__main__':
    unittest.main()
