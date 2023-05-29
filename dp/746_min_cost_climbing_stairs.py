import unittest
from typing import List

"""

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.


Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999


"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        prev = cost[0]
        curr = cost[1]

        for i in range(2, len(cost)):

            temp = curr
            curr = cost[i] + min(prev, curr)
            prev = temp

        return min(prev,curr)

        # # array captures lowest values to reach a step
        # lowest = [cost[0], cost[1]]

        # # iterate thru steps starting from step 3
        # for step in range(2, len(cost), 1):

        #     # append step value + min of previous 2 steps
        #     lowest.append(cost[step] + min(lowest[step-1], lowest[step-2]))

        # # return min of last 2 values in array
        # return min(lowest[-1], lowest[-2])

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minCostClimbingStairs_example1(self):
        cost = [10, 15, 20]
        result = self.solution.minCostClimbingStairs(cost)
        self.assertEqual(result, 15)

    def test_minCostClimbingStairs_example2(self):
        cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        result = self.solution.minCostClimbingStairs(cost)
        self.assertEqual(result, 6)

    def test_minCostClimbingStairs_custom1(self):
        cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = self.solution.minCostClimbingStairs(cost)
        self.assertEqual(result, 25)

    def test_minCostClimbingStairs_custom2(self):
        cost = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        result = self.solution.minCostClimbingStairs(cost)
        self.assertEqual(result, 250)

    def test_minCostClimbingStairs_custom3(self):
        cost = [2, 2, 1, 1, 2, 2, 1, 1, 2, 2]
        result = self.solution.minCostClimbingStairs(cost)
        self.assertEqual(result, 8)

if __name__ == '__main__':
    unittest.main()
