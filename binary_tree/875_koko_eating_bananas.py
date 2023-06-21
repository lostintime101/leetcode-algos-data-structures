import unittest
from typing import List
import math

"""

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.


Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109

"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        ret = max(piles)
        l, r = 0, ret

        def check(g):
            count = 0
            for pile in piles:
                count += math.ceil(pile / g)
            if count <= h: return True
            return False

        while l <= r:
            guess = (l + r) // 2

            if check(guess):
                if guess == 1:
                    return guess
                elif not check(guess - 1):
                    return guess
                else:
                    r = guess - 1
            else:
                l = guess + 1

        return guess


class TestSolution(unittest.TestCase):
    def test_minEatingSpeed(self):
        solution = Solution()

        piles = [3, 6, 7, 11]
        h = 8
        expected = 4
        self.assertEqual(solution.minEatingSpeed(piles, h), expected)

        piles = [30, 11, 23, 4, 20]
        h = 5
        expected = 30
        self.assertEqual(solution.minEatingSpeed(piles, h), expected)

        piles = [30, 11, 23, 4, 20]
        h = 6
        expected = 23
        self.assertEqual(solution.minEatingSpeed(piles, h), expected)

        piles = [30, 11, 23, 4, 20]
        h = 9
        expected = 12
        self.assertEqual(solution.minEatingSpeed(piles, h), expected)

        piles = [30, 11, 23, 4, 20]
        h = 1
        expected = 30
        self.assertEqual(solution.minEatingSpeed(piles, h), expected)

if __name__ == '__main__':
    unittest.main()
