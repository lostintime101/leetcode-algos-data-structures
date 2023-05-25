import unittest
from typing import List
"""
You are given an array of non-overlapping intervals where intervals[i] = [starti, endi] represent the
start and the end of the ith interval and intervals is sorted in ascending order by starti.
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and
intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105

"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # INTERVALS SOLUTION
        ret = []
        for interval in intervals:

            if interval[0] > newInterval[1] or interval[1] < newInterval[0]:
                ret.append(interval)
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        ret.append(newInterval)

        return sorted(ret)

        # ORIGINAL PASS
        # overlaps, ret = [newInterval], []
        # start, fin = newInterval[0], newInterval[1]

        # for interval in intervals:
        #     s = interval[0]
        #     f = interval[1]

        #     if ((s < start) and (f >= start)) or ((s >= start) and (f <= fin)) or ((s <= fin) and (f >= fin)):
        #         overlaps.append(interval)
        #     else: ret.append(interval)

        # newStart = overlaps[0][0]
        # newFin = overlaps[0][1]

        # for overlap in overlaps:
        #     newStart = min(newStart, overlap[0])
        #     newFin = max(newFin, overlap[1])

        # ret.append([newStart, newFin])

        # return sorted(ret)


class TestInsertIntervals(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_insert_intervals(self):
        # Test case where new interval does not overlap with any existing intervals
        intervals1 = [[1, 3], [6, 9]]
        newInterval1 = [2, 5]
        expected1 = [[1, 5], [6, 9]]
        self.assertEqual(self.solution.insert(intervals1, newInterval1), expected1)

        # Test case where new interval overlaps with existing intervals
        intervals2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        newInterval2 = [4, 9]
        expected2 = [[1, 2], [3, 10], [12, 16]]
        self.assertEqual(self.solution.insert(intervals2, newInterval2), expected2)

        # Test case where new interval is completely within an existing interval
        intervals3 = [[1, 5], [6, 8]]
        newInterval3 = [2, 4]
        expected3 = [[1, 5], [6, 8]]
        self.assertEqual(self.solution.insert(intervals3, newInterval3), expected3)

        # Test case where new interval is before all existing intervals
        intervals4 = [[3, 6], [9, 12]]
        newInterval4 = [1, 2]
        expected4 = [[1, 2], [3, 6], [9, 12]]
        self.assertEqual(self.solution.insert(intervals4, newInterval4), expected4)

        # Test case where new interval is after all existing intervals
        intervals5 = [[2, 4], [6, 8]]
        newInterval5 = [9, 10]
        expected5 = [[2, 4], [6, 8], [9, 10]]
        self.assertEqual(self.solution.insert(intervals5, newInterval5), expected5)

if __name__ == '__main__':
    unittest.main()
