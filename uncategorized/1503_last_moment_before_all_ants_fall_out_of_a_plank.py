import unittest
from typing import List

"""

We have a wooden plank of the length n units. Some ants are walking on the plank, each ant moves with a speed of 1 unit per second. Some of the ants move to the left, the other move to the right.

When two ants moving in two different directions meet at some point, they change their directions and continue moving again. Assume changing directions does not take any additional time.

When an ant reaches one end of the plank at a time t, it falls out of the plank immediately.

Given an integer n and two integer arrays left and right, the positions of the ants moving to the left and the right, return the moment when the last ant(s) fall out of the plank.

Constraints:

1 <= n <= 104
0 <= left.length <= n + 1
0 <= left[i] <= n
0 <= right.length <= n + 1
0 <= right[i] <= n
1 <= left.length + right.length <= n + 1
All values of left and right are unique, and each value can appear only in one of the two arrays.

"""


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:

        right = [(n - num) for num in right]
        if right and left:
            return max(max(left), max(right))
        if right:
            return max(right)


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        n = 10
        left = [4, 5]
        right = [7, 2]
        self.assertEqual(self.solution.getLastMoment(n, left, right), 8)

    def test_case_2(self):
        n = 5
        left = []
        right = [3, 4]
        self.assertEqual(self.solution.getLastMoment(n, left, right), 2)

    def test_case_3(self):
        n = 7
        left = [2, 6]
        right = []
        self.assertEqual(self.solution.getLastMoment(n, left, right), None)

    def test_case_4(self):
        n = 3
        left = []
        right = []
        self.assertEqual(self.solution.getLastMoment(n, left, right), None)


if __name__ == '__main__':
    unittest.main()
