import unittest

"""

There are n people standing in a line labeled from 1 to n. The first person in the line is holding a pillow initially. Every second, the person holding the pillow passes it to the next person standing in the line. Once the pillow reaches the end of the line, the direction changes, and people continue passing the pillow in the opposite direction.

For example, once the pillow reaches the nth person they pass it to the n - 1th person, then to the n - 2th person and so on.
Given the two positive integers n and time, return the index of the person holding the pillow after time seconds.

Constraints:

2 <= n <= 1000
1 <= time <= 1000

"""

class Solution:
    def passThePillow(self, n: int, time: int) -> int:

        # Simulation version

        # curr = 1
        # forward = True

        # while time:

        #     if curr == n: forward = False
        #     if curr == 1: forward = True

        #     if forward: curr += 1
        #     if not forward: curr -= 1

        #     time -= 1

        # return curr

        # Math version

        place = time % (n - 1)
        rounds = time // (n - 1)

        if rounds % 2:
            return n - place
        else:
            return 1 + place


class TestPassThePillow(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_pass_the_pillow(self):
        self.assertEqual(self.solution.passThePillow(5, 0), 1)
        self.assertEqual(self.solution.passThePillow(5, 1), 2)
        self.assertEqual(self.solution.passThePillow(5, 2), 3)
        self.assertEqual(self.solution.passThePillow(5, 3), 4)
        self.assertEqual(self.solution.passThePillow(5, 4), 5)
        self.assertEqual(self.solution.passThePillow(5, 5), 4)
        self.assertEqual(self.solution.passThePillow(5, 6), 3)
        self.assertEqual(self.solution.passThePillow(5, 7), 2)
        self.assertEqual(self.solution.passThePillow(5, 8), 1)
        self.assertEqual(self.solution.passThePillow(5, 9), 2)

        self.assertEqual(self.solution.passThePillow(3, 0), 1)
        self.assertEqual(self.solution.passThePillow(3, 1), 2)
        self.assertEqual(self.solution.passThePillow(3, 2), 3)
        self.assertEqual(self.solution.passThePillow(3, 3), 2)
        self.assertEqual(self.solution.passThePillow(3, 4), 1)
        self.assertEqual(self.solution.passThePillow(3, 5), 2)
        self.assertEqual(self.solution.passThePillow(3, 6), 3)
        self.assertEqual(self.solution.passThePillow(3, 7), 2)

    def test_edge_cases(self):
        self.assertEqual(self.solution.passThePillow(2, 0), 1)
        self.assertEqual(self.solution.passThePillow(2, 1), 2)
        self.assertEqual(self.solution.passThePillow(2, 2), 1)

        self.assertEqual(self.solution.passThePillow(4, 10), 3)
        self.assertEqual(self.solution.passThePillow(4, 11), 2)
        self.assertEqual(self.solution.passThePillow(4, 12), 1)
        self.assertEqual(self.solution.passThePillow(4, 13), 2)


if __name__ == '__main__':
    unittest.main()
