import unittest
from functools import cache
from typing import List

"""

A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.

Constraints:

2 <= stones.length <= 2000
0 <= stones[i] <= 231 - 1
stones[0] == 0
stones is sorted in a strictly increasing order.


"""


class Solution:
    def canCross(self, stones: List[int]) -> bool:

        ans = [False]

        @cache
        def jump(stone, speed):

            if stone == len(stones) - 1:
                ans[0] = True
                return

            if stone == 0:
                speeds = [speed]
            elif speed == 1:
                speeds = [speed, speed + 1]
            else:
                speeds = [speed - 1, speed, speed + 1]

            for sp in speeds:

                next_stone = stones[stone] + sp
                for i in range(stone, len(stones)):

                    if stones[i] == next_stone:
                        jump(i, sp)
                        break
                    if stones[i] > next_stone: break

        jump(0, 1)

        return ans[0]



class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        stones = [0, 1, 3, 5, 6, 8, 12, 17]
        self.assertTrue(self.solution.canCross(stones))

    def test_case_2(self):
        stones = [0, 1, 2, 3, 4, 8, 9, 11]
        self.assertFalse(self.solution.canCross(stones))

    def test_case_3(self):
        stones = [0, 1, 3, 6, 10, 15, 21]
        self.assertTrue(self.solution.canCross(stones))

    def test_case_4(self):
        stones = [0, 1, 3, 4, 5, 7, 9, 10, 12]
        self.assertTrue(self.solution.canCross(stones))

    def test_case_5(self):
        stones = [0, 1, 3, 5, 6, 8, 12, 14, 19]
        self.assertFalse(self.solution.canCross(stones))


if __name__ == '__main__':
    unittest.main()
