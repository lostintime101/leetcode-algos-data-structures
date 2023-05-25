import unittest

"""

Description
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
determine if a person could attend all meetings.

"""

def can_attend_meetings(intervals) -> bool:

    if len(intervals) == 1: return True
    ret = []
    intervals = sorted(intervals)

    prev = intervals[0]

    for i in range(1, len(intervals)):
        curr = intervals[i]

        if curr[0] > prev[1]:
            ret.append(prev)
        else:
            return False
        prev = curr

    return True

import unittest

class TestCanAttendMeetings(unittest.TestCase):

    def test_can_attend_meetings(self):
        # Test case where all intervals are non-overlapping
        intervals1 = [(1, 2), (3, 4), (5, 6)]
        self.assertTrue(can_attend_meetings(intervals1))

        # Test case where intervals overlap
        intervals2 = [(1, 3), (2, 4), (3, 5)]
        self.assertFalse(can_attend_meetings(intervals2))

        # Test case with single interval
        intervals3 = [(1, 2)]
        self.assertTrue(can_attend_meetings(intervals3))

        # Test case with overlapping intervals
        intervals5 = [(1, 4), (2, 5), (3, 6)]
        self.assertFalse(can_attend_meetings(intervals5))

        # Test case with intervals in reverse order
        intervals6 = [(5, 6), (3, 4), (1, 2)]
        self.assertTrue(can_attend_meetings(intervals6))

if __name__ == '__main__':
    unittest.main()
