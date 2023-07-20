import unittest
from typing import List

"""

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Constraints:

2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0

"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for asteroid in asteroids:

            # positive value or empty stack array
            if (not stack) or (asteroid > 0):
                stack.append(asteroid)
                continue

            while True:

                if stack[-1] < 0:
                    stack.append(asteroid)
                    break
                elif stack[-1] == abs(asteroid):
                    stack.pop()
                    break
                elif stack[-1] > abs(asteroid):
                    break

                stack.pop()

                if not stack:
                    stack.append(asteroid)
                    break

        return stack


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_asteroidCollision_case1(self):
        asteroids = [5, 10, -5]
        self.assertEqual(self.solution.asteroidCollision(asteroids), [5, 10])

    def test_asteroidCollision_case2(self):
        asteroids = [8, -8]
        self.assertEqual(self.solution.asteroidCollision(asteroids), [])

    def test_asteroidCollision_case3(self):
        asteroids = [10, 2, -5]
        self.assertEqual(self.solution.asteroidCollision(asteroids), [10])

    def test_asteroidCollision_case4(self):
        asteroids = [-2, -1, 1, 2]
        self.assertEqual(self.solution.asteroidCollision(asteroids), [-2, -1, 1, 2])

    def test_asteroidCollision_case5(self):
        asteroids = [1, -2, -2, -1]
        self.assertEqual(self.solution.asteroidCollision(asteroids), [-2, -2, -1])


if __name__ == "__main__":
    unittest.main()
