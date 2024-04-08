import unittest
from typing import List

"""
The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
Otherwise, they will leave it and go to the queue's end.
This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.

Constraints:

1 <= students.length, sandwiches.length <= 100
students.length == sandwiches.length
sandwiches[i] is 0 or 1.
students[i] is 0 or 1.

"""

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        curr_sand = 0
        N = len(students)
        M = len(sandwiches)
        ans = N
        last_ans = N

        while True:
            for i in range(N):
                if students[i] == sandwiches[curr_sand]:
                    students[i] = -1
                    ans -= 1
                    curr_sand += 1
                    if ans == 0:
                        return 0

            if last_ans == ans:
                return ans
            last_ans = ans


class TestSolution(unittest.TestCase):
    def test_countStudents(self):
        solution = Solution()

        # Test case with students and sandwiches of the same order
        students = [1, 1, 0, 0]
        sandwiches = [1, 1, 0, 0]
        self.assertEqual(solution.countStudents(students, sandwiches), 0)

        # Test case with students and sandwiches of different order
        students = [1, 1, 1, 0, 0, 1]
        sandwiches = [1, 1, 0, 0, 1, 0]
        self.assertEqual(solution.countStudents(students, sandwiches), 1)

        # Test case with students preferring different sandwiches
        students = [1, 0, 0, 1, 1]
        sandwiches = [0, 1, 1, 0, 0]
        self.assertEqual(solution.countStudents(students, sandwiches), 1)

        # Test case with all students preferring the same sandwich
        students = [0, 0, 0, 0]
        sandwiches = [0, 0, 0, 0]
        self.assertEqual(solution.countStudents(students, sandwiches), 0)

        # Test case with empty lists
        students = []
        sandwiches = []
        self.assertEqual(solution.countStudents(students, sandwiches), 0)


if __name__ == "__main__":
    unittest.main()
