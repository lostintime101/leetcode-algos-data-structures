import unittest
from typing import List
from collections import defaultdict

"""

There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.

You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.

It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.

Return the original array nums. If there are multiple solutions, return any of them.

Constraints:

nums.length == n
adjacentPairs.length == n - 1
adjacentPairs[i].length == 2
2 <= n <= 105
-105 <= nums[i], ui, vi <= 105
There exists some nums that has adjacentPairs as its pairs.

"""

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        neighbors = defaultdict(list)

        # build dict of neighbors
        for pair in adjacentPairs:
            neighbors[pair[0]].append(pair[1])
            neighbors[pair[1]].append(pair[0])

        ret = [0] * len(neighbors)

        # find one of the ends
        for k, v in neighbors.items():
            if len(v) == 1:
                ret[0] = k
                ret[1] = neighbors[k][0]
                break

        # match up the rest of the list
        for i in range(2, len(ret)):
            if neighbors[ret[i - 1]][0] != ret[i - 2]:
                ret[i] = neighbors[ret[i - 1]][0]
            else:
                ret[i] = neighbors[ret[i - 1]][1]

        return ret


class TestRestoreArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_restore_array_basic(self):
        adjacentPairs = [[2, 1], [3, 4], [3, 2]]
        result = self.solution.restoreArray(adjacentPairs)
        self.assertEqual(result, [1, 2, 3, 4])

    def test_restore_array_longer(self):
        adjacentPairs = [[4, 3], [2, 1], [3, 2], [5, 4]]
        result = self.solution.restoreArray(adjacentPairs)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_restore_array_duplicate_pairs(self):
        adjacentPairs = [[2, 1], [3, 4], [3, 2], [4, 3]]
        result = self.solution.restoreArray(adjacentPairs)
        self.assertEqual(result, [1, 2, 3, 4])

    def test_restore_array_single_element(self):
        adjacentPairs = [[1, 2]]
        result = self.solution.restoreArray(adjacentPairs)
        self.assertEqual(result, [1, 2])


if __name__ == '__main__':
    unittest.main()
