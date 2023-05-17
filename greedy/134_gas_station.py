import unittest

"""
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its 
next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit 
once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

Constraints:

n == gas.length == cost.length
1 <= n <= 105
0 <= gas[i], cost[i] <= 104

"""

class Solution:
    def canCompleteCircuit(self, gas: [int], cost: [int]) -> int:

        total, start_index, local_total = 0, 0, 0

        for i in range(len(gas)):

            comb = gas[i] - cost[i]
            total += comb

            if local_total <= 0:
                start_index = i
                local_total = comb
            else:
                local_total += comb

        if total < 0: return -1
        return start_index


class TestSolution(unittest.TestCase):

    def test_canCompleteCircuit(self):
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        expected = 3
        solution = Solution()
        self.assertEqual(solution.canCompleteCircuit(gas, cost), expected)

        gas = [2, 3, 4]
        cost = [3, 4, 3]
        expected = -1
        solution = Solution()
        self.assertEqual(solution.canCompleteCircuit(gas, cost), expected)

        gas = [5, 1, 2, 3, 4]
        cost = [4, 4, 1, 5, 1]
        expected = 4
        solution = Solution()
        self.assertEqual(solution.canCompleteCircuit(gas, cost), expected)


if __name__ == '__main__':
    unittest.main()
