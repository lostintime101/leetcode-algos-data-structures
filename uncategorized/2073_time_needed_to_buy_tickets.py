from typing import List
import unittest

"""
There are n people in a line queuing to buy tickets, where the 0th person is at the front of the line and the (n - 1)th person is at the back of the line.

You are given a 0-indexed integer array tickets of length n where the number of tickets that the ith person would like to buy is tickets[i].

Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and has to go back to the end of the line (which happens instantaneously) in order to buy more tickets. If a person does not have any tickets left to buy, the person will leave the line.

Return the time taken for the person at position k (0-indexed) to finish buying tickets.

"""

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        ans = 0

        for i, v in enumerate(tickets):
            if i <= k:
                ans += min(v, tickets[k])
            else:
                ans += min(v, tickets[k] - 1)

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_timeRequiredToBuy_case1(self):
        tickets = [1, 2, 3, 4, 5]
        k = 2
        expected = 10
        self.assertEqual(self.solution.timeRequiredToBuy(tickets, k), expected)

    def test_timeRequiredToBuy_case2(self):
        tickets = [5, 4, 3, 2, 1]
        k = 1
        expected = 14
        self.assertEqual(self.solution.timeRequiredToBuy(tickets, k), expected)

    def test_timeRequiredToBuy_case3(self):
        tickets = [1, 1, 1, 1, 1]
        k = 0
        expected = 1
        self.assertEqual(self.solution.timeRequiredToBuy(tickets, k), expected)

    def test_timeRequiredToBuy_case4(self):
        tickets = [10, 20, 30, 40, 50]
        k = 3
        expected = 139
        self.assertEqual(self.solution.timeRequiredToBuy(tickets, k), expected)


if __name__ == '__main__':
    unittest.main()
