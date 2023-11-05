import unittest
from typing import List

"""

Given an integer array arr of distinct integers and an integer k.

A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]). In each round of the game, we compare arr[0] with arr[1], the larger integer wins and remains at position 0, and the smaller integer moves to the end of the array. The game ends when an integer wins k consecutive rounds.

Return the integer which will win the game.

It is guaranteed that there will be a winner of the game.

Constraints:

2 <= arr.length <= 105
1 <= arr[i] <= 106
arr contains distinct integers.
1 <= k <= 109

"""


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:

        l, r = 0, 1
        curr, count = 0, 0

        while r < len(arr):
            if arr[l] > arr[r]:
                r += 1
                count += 1
            else:
                l = r
                curr = r
                r = l + 1
                count = 1
            if count >= k:
                return arr[curr]

        return arr[curr]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_getWinner(self):
        # Test case 1
        arr1 = [2, 1, 3, 5, 4, 6, 7]
        k1 = 2
        self.assertEqual(self.solution.getWinner(arr1, k1), 5)

        # Test case 2
        arr2 = [3, 2, 1]
        k2 = 10
        self.assertEqual(self.solution.getWinner(arr2, k2), 3)

        # Test case 3
        arr3 = [1, 9, 8, 2, 3, 7, 6, 4, 5]
        k3 = 4
        self.assertEqual(self.solution.getWinner(arr3, k3), 9)

        # Test case 4 (edge case with minimum k value)
        arr4 = [1, 2, 3, 4, 5]
        k4 = 1
        self.assertEqual(self.solution.getWinner(arr4, k4), 2)

        # Test case 5 (edge case with maximum k value)
        arr5 = [5, 4, 3, 2, 1]
        k5 = 5
        self.assertEqual(self.solution.getWinner(arr5, k5), 5)


if __name__ == '__main__':
    unittest.main()
