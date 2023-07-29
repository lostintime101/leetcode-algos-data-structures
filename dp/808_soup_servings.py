import unittest
from functools import cache

"""

There are two types of soup: type A and type B. Initially, we have n ml of each type of soup. There are four kinds of operations:

Serve 100 ml of soup A and 0 ml of soup B,
Serve 75 ml of soup A and 25 ml of soup B,
Serve 50 ml of soup A and 50 ml of soup B, and
Serve 25 ml of soup A and 75 ml of soup B.
When we serve some soup, we give it to someone, and we no longer have it. Each turn, we will choose from the four operations with an equal probability 0.25. If the remaining volume of soup is not enough to complete the operation, we will serve as much as possible. We stop once we no longer have some quantity of both types of soup.

Note that we do not have an operation where all 100 ml's of soup B are used first.

Return the probability that soup A will be empty first, plus half the probability that A and B become empty at the same time. Answers within 10-5 of the actual answer will be accepted.

Constraints:

0 <= n <= 109

"""


class Solution:
    def soupServings(self, n: int) -> float:

        if n >= 5000: return 1

        @cache
        def serve(a, b):

            if (a <= 0) and (b <= 0): return 0.5
            elif a <= 0: return 1
            elif b <= 0: return 0

            return (serve(a - 100, b) * 0.25) + (serve(a - 75, b - 25) * 0.25) + (serve(a - 50, b - 50) * 0.25) + (
                        serve(a - 25, b - 75) * 0.25)

        return serve(n, n)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_soupServings(self):
        # Test cases with small input values
        self.assertAlmostEqual(self.solution.soupServings(0), 0.5, delta=1e-5)
        self.assertAlmostEqual(self.solution.soupServings(1), 0.625, delta=1e-5)
        self.assertAlmostEqual(self.solution.soupServings(10), 0.625, delta=1e-5)
        self.assertAlmostEqual(self.solution.soupServings(20), 0.625, delta=1e-5)

        # Test case with a larger input value
        self.assertAlmostEqual(self.solution.soupServings(100), 0.71875, delta=1e-5)

        # Test case where n >= 5000, the function should return 1
        self.assertAlmostEqual(self.solution.soupServings(5000), 1.0, delta=1e-5)
        self.assertAlmostEqual(self.solution.soupServings(10000), 1.0, delta=1e-5)

        # Test cases with edge and corner values
        self.assertAlmostEqual(self.solution.soupServings(150), 0.7578125, delta=1e-5)
        self.assertAlmostEqual(self.solution.soupServings(250), 0.82763671875, delta=1e-5)
        self.assertAlmostEqual(self.solution.soupServings(500), 0.916344165802002, delta=1e-5)


if __name__ == "__main__":
    unittest.main()
