import unittest
from typing import List

"""

You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

Return the length longest chain which can be formed.

You do not need to use up all the given intervals. You can select pairs in any order.

Constraints:

n == pairs.length
1 <= n <= 1000
-1000 <= lefti < righti <= 1000

"""


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        # sort pairs by second "end" value
        pairs = sorted(pairs, key=lambda x: x[-1])

        # start with lowest pair
        ans = 1
        curr = pairs[0][1]

        for pair in pairs:

            start, end = pair[0], pair[1]

            # skip if it overlaps
            if start <= curr:
                continue

            # set the new current end value
            else:
                curr = end
                ans += 1

        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        pairs = [[1, 2], [2, 3], [3, 4]]
        self.assertEqual(self.solution.findLongestChain(pairs), 2)

    def test_single_pair(self):
        pairs = [[1, 2]]
        self.assertEqual(self.solution.findLongestChain(pairs), 1)

    def test_overlapping_pairs(self):
        pairs = [[1, 3], [2, 4], [3, 5]]
        self.assertEqual(self.solution.findLongestChain(pairs), 1)

    def test_disjoint_pairs(self):
        pairs = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(self.solution.findLongestChain(pairs), 3)

    def test_mixed_pairs(self):
        pairs = [[1, 6], [2, 3], [3, 4], [5, 7], [6, 8]]
        self.assertEqual(self.solution.findLongestChain(pairs), 2)


if __name__ == '__main__':
    unittest.main()
