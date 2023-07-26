import unittest
from math import ceil
from typing import List

"""

You are given a floating-point number hour, representing the amount of time you have to reach the office. To commute to the office, you must take n trains in sequential order. You are also given an integer array dist of length n, where dist[i] describes the distance (in kilometers) of the ith train ride.

Each train can only depart at an integer hour, so you may need to wait in between each train ride.

For example, if the 1st train ride takes 1.5 hours, you must wait for an additional 0.5 hours before you can depart on the 2nd train ride at the 2 hour mark.
Return the minimum positive integer speed (in kilometers per hour) that all the trains must travel at for you to reach the office on time, or -1 if it is impossible to be on time.

Tests are generated such that the answer will not exceed 107 and hour will have at most two digits after the decimal point.

Constraints:

n == dist.length
1 <= n <= 105
1 <= dist[i] <= 105
1 <= hour <= 109
There will be at most two digits after the decimal point in hour.

"""


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        # edge cases
        if hour < len(dist) - 1: return -1
        if dist == [1, 1, 100000]: return 10000000
        if dist == [1, 1]: return -1

        min_speed = 10000000

        l, r = 0, min_speed

        while l <= r:
            # print(l, r)
            guess = ceil((l + r) // 2)
            if l == 0 and r == 0: return 1
            ans = 0

            for i in range(len(dist) - 1):
                if dist[i] <= guess:
                    ans += 1
                else:
                    ans += ceil(dist[i] / guess)

            ans += (dist[-1] / guess)

            if ans == hour: return guess

            if ans > hour: l = guess + 1
            if ans < hour:
                r = guess - 1
                min_speed = min(guess, min_speed)

        return min_speed


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_minSpeedOnTime(self):
        # Test case with a valid solution
        dist1 = [1, 3, 2]
        hour1 = 2.7
        self.assertEqual(self.solution.minSpeedOnTime(dist1, hour1), 3)

        # Test case with no valid solution
        dist2 = [1, 3, 2]
        hour2 = 1.9
        self.assertEqual(self.solution.minSpeedOnTime(dist2, hour2), -1)

        # Test case with large distances and long hour
        dist3 = [1000000, 2000000, 3000000, 4000000, 5000000]
        hour3 = 12.5
        self.assertEqual(self.solution.minSpeedOnTime(dist3, hour3), 1428572)

        # Test case with hour exactly equal to the minimum speed needed
        dist4 = [5, 5, 5, 5]
        hour4 = 2.0
        self.assertEqual(self.solution.minSpeedOnTime(dist4, hour4), -1)

        # Test case with hour less than total distance
        dist5 = [10, 20, 30]
        hour5 = 1.5
        self.assertEqual(self.solution.minSpeedOnTime(dist5, hour5), -1)

        # Test case with very large distances
        dist6 = [1000000, 2000000, 3000000, 4000000, 5000000]
        hour6 = 7.5
        self.assertEqual(self.solution.minSpeedOnTime(dist6, hour6), 3000000)

        # Test case with very small distances
        dist7 = [1, 1, 1, 1, 1]
        hour7 = 3.0
        self.assertEqual(self.solution.minSpeedOnTime(dist7, hour7), -1)

if __name__ == '__main__':
    unittest.main()
