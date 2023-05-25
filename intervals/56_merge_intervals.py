import unittest
from typing import List

"""

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # INTERVALS SOLUTION
        if len(intervals) == 1: return intervals

        ret = []
        intervals = sorted(intervals)
        prev = intervals[0]

        for i in range(1, len(intervals)):

            curr = intervals[i]
            if curr[0] > prev[1]:
                ret.append(prev)
                prev = curr
            else:
                prev[0] = min(curr[0], prev[0])
                prev[1] = max(curr[1], prev[1])

        ret.append(prev)

        return ret


class TestMergeIntervals(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_merge_intervals(self):
        # Test case where intervals do not overlap
        intervals1 = [[1, 3], [4, 6], [7, 9]]
        expected1 = [[1, 3], [4, 6], [7, 9]]
        self.assertEqual(self.solution.merge(intervals1), expected1)

        # Test case where intervals overlap and can be merged
        intervals2 = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected2 = [[1, 6], [8, 10], [15, 18]]
        self.assertEqual(self.solution.merge(intervals2), expected2)

        # Test case where intervals overlap and can be fully merged
        intervals3 = [[1, 4], [4, 5]]
        expected3 = [[1, 5]]
        self.assertEqual(self.solution.merge(intervals3), expected3)

        # Test case where intervals are already merged
        intervals4 = [[1, 5], [6, 9], [10, 15]]
        expected4 = [[1, 5], [6, 9], [10, 15]]
        self.assertEqual(self.solution.merge(intervals4), expected4)

        # Test case where intervals have reverse order
        intervals5 = [[6, 9], [4, 5], [1, 3]]
        expected5 = [[1, 3], [4, 5], [6,9]]
        self.assertEqual(self.solution.merge(intervals5), expected5)

        # Test case where intervals have single interval
        intervals6 = [[2, 4]]
        expected6 = [[2, 4]]
        self.assertEqual(self.solution.merge(intervals6), expected6)

if __name__ == '__main__':
    unittest.main()


