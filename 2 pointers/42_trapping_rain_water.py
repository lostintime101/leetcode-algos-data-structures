import unittest
from typing import List

"""

Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105

"""

class Solution:
    def trap(self, height: List[int]) -> int:

        ret = 0
        maxLeft, maxRight = 0, 0
        Lmax, Rmax = [], []

        for val in height:
            maxLeft = max(maxLeft, val)
            Lmax.append(maxLeft)

        for val in height[::-1]:
            maxRight = max(maxRight, val)
            Rmax.append(maxRight)
        Rmax = Rmax[::-1]

        for i, v in enumerate(height):
            x = min(Lmax[i], Rmax[i]) - v
            if x > 0: ret += x

        return ret


class SolutionTests(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_trap_example1(self):
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        expected = 6
        actual = self.solution.trap(height)
        self.assertEqual(actual, expected)

    def test_trap_example2(self):
        height = [4, 2, 0, 3, 2, 5]
        expected = 9
        actual = self.solution.trap(height)
        self.assertEqual(actual, expected)

    def test_trap_empty_height(self):
        height = []
        expected = 0
        actual = self.solution.trap(height)
        self.assertEqual(actual, expected)

    def test_trap_all_same_height(self):
        height = [1, 1, 1, 1, 1]
        expected = 0
        actual = self.solution.trap(height)
        self.assertEqual(actual, expected)

    def test_trap_ascending_height(self):
        height = [1, 2, 3, 4, 5]
        expected = 0
        actual = self.solution.trap(height)
        self.assertEqual(actual, expected)

    def test_trap_descending_height(self):
        height = [5, 4, 3, 2, 1]
        expected = 0
        actual = self.solution.trap(height)
        self.assertEqual(actual, expected)

    def test_trap_single_element_height(self):
        height = [5]
        expected = 0
        actual = self.solution.trap(height)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
