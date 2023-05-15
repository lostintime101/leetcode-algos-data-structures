import heapq

"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. 
Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

Constraints:

1 <= stones.length <= 30
1 <= stones[i] <= 1000

"""


class Solution:
    def lastStoneWeight(self, stones: [int]) -> int:
        # HEAPIFY SOLUTION

        stones = [stone * -1 for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            s1 -= s2
            heapq.heappush(stones, s1)

        return heapq.heappop(stones) * -1

        # # stop sequence when only 1 stone left
        # while len(stones) > 1:

        #     # sort stones big to small
        #     stones = sorted(stones)[::-1]

        #     # smash 2 biggest stones together
        #     new_stone = stones[0] - stones[1]

        #     # remove 2 biggest stones from list
        #     stones = stones[2::]

        #     # append new stone to list
        #     stones.append(new_stone)

        # return stones[0]

import unittest

class SolutionTests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_lastStoneWeight(self):
        stones = [2, 7, 4, 1, 8, 1]
        result = self.solution.lastStoneWeight(stones)
        self.assertEqual(result, 1, "Incorrect result for test case 1")

        stones = [5, 5, 5, 5, 5]
        result = self.solution.lastStoneWeight(stones)
        self.assertEqual(result, 5, "Incorrect result for test case 2")

        stones = [1, 2, 3, 4, 5]
        result = self.solution.lastStoneWeight(stones)
        self.assertEqual(result, 1, "Incorrect result for test case 3")

        stones = [10, 10, 10, 10]
        result = self.solution.lastStoneWeight(stones)
        self.assertEqual(result, 0, "Incorrect result for test case 4")

        stones = [2, 2, 4, 8, 16]
        result = self.solution.lastStoneWeight(stones)
        self.assertEqual(result, 0, "Incorrect result for test case 5")

if __name__ == "__main__":
    unittest.main()
