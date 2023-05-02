import unittest

"""
There are n cars going to the same destination along a one-lane road. The destination is target miles away.

You are given two integer array position and speed, both of length n, where position[i] is the position of the
ith car and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed.
The faster car will slow down to match the slower car's speed.
The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed.
Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.

Constraints:

n == position.length == speed.length
1 <= n <= 105
0 < target <= 106
0 <= position[i] < target
All the values of position are unique.
0 < speed[i] <= 106
"""


class Solution:
    def carFleet(self, target: int, position: [int], speed: [int]) -> int:

        ret = len(position)

        sort_pos = sorted(list(zip(position, speed)), reverse=True)

        slowest = 0

        for i in sort_pos:

            t = (target - i[0]) / i[1]

            if t <= slowest:
                ret -= 1
            else:
                slowest = t

        return ret


class TestSolution(unittest.TestCase):

    def test_carFleet(self):
        solution = Solution()

        # Test case 1
        target1 = 12
        position1 = [10, 8, 0, 5, 3]
        speed1 = [2, 4, 1, 1, 3]
        expected1 = 3
        self.assertEqual(solution.carFleet(target1, position1, speed1), expected1)

        # Test case 2
        target2 = 25
        position2 = [4, 3, 10, 1, 6]
        speed2 = [2, 4, 1, 1, 3]
        expected2 = 2
        self.assertEqual(solution.carFleet(target2, position2, speed2), expected2)

        # Test case 3
        target3 = 70
        position3 = [0, 10, 20, 30, 40, 50, 60]
        speed3 = [2, 2, 2, 2, 2, 2, 2]
        expected3 = 7
        self.assertEqual(solution.carFleet(target3, position3, speed3), expected3)


if __name__ == '__main__':
    unittest.main()
