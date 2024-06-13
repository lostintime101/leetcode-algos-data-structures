import unittest
from typing import List

"""

There are n seats and n students in a room. You are given an array seats of length n, where seats[i] is the position of the ith seat. You are also given the array students of length n, where students[j] is the position of the jth student.

You may perform the following move any number of times:

Increase or decrease the position of the ith student by 1 (i.e., moving the ith student from position x to x + 1 or x - 1)
Return the minimum number of moves required to move each student to a seat such that no two students are in the same seat.

Note that there may be multiple seats or students in the same position at the beginning.

Constraints:

n == seats.length == students.length
1 <= n <= 100
1 <= seats[i], students[j] <= 100

"""

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats = sorted(seats)
        students = sorted(students)

        return sum([abs(seats[i] - students[i]) for i in range(len(seats))])


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_typical_case(self):
        seats = [3, 1, 4]
        students = [2, 3, 1]
        self.assertEqual(self.solution.minMovesToSeat(seats, students), 2)

    def test_already_seated(self):
        seats = [1, 2, 3]
        students = [1, 2, 3]
        self.assertEqual(self.solution.minMovesToSeat(seats, students), 0)

    def test_reverse_order(self):
        seats = [1, 2, 3]
        students = [3, 2, 1]
        self.assertEqual(self.solution.minMovesToSeat(seats, students), 0)

    def test_large_numbers(self):
        seats = [100, 200, 300]
        students = [150, 250, 350]
        self.assertEqual(self.solution.minMovesToSeat(seats, students), 150)

    def test_single_element(self):
        seats = [5]
        students = [10]
        self.assertEqual(self.solution.minMovesToSeat(seats, students), 5)

    def test_empty_lists(self):
        seats = []
        students = []
        self.assertEqual(self.solution.minMovesToSeat(seats, students), 0)

    def test_same_values(self):
        seats = [1, 1, 1]
        students = [1, 1, 1]
        self.assertEqual(self.solution.minMovesToSeat(seats, students), 0)

    def test_unordered_lists(self):
        seats = [10, 20, 30, 40]
        students = [15, 35, 25, 5]
        self.assertEqual(self.solution.minMovesToSeat(seats, students), 20)


if __name__ == '__main__':
    unittest.main()