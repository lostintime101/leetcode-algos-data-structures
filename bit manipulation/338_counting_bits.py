import unittest
from typing import List

"""

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
ans[i] is the number of 1's in the binary representation of i.

Constraints:

0 <= n <= 105

"""

class Solution:
    def countBits(self, n: int) -> List[int]:

        return [len([bit for bit in bin(num) if bit == "1"]) for num in range(0,n+1)]



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_countBits(self):
        # Test case 1: n = 2
        result = self.solution.countBits(2)
        self.assertEqual(result, [0, 1, 1])

        # Test case 2: n = 5
        result = self.solution.countBits(5)
        self.assertEqual(result, [0, 1, 1, 2, 1, 2])

        # Test case 3: n = 0
        result = self.solution.countBits(0)
        self.assertEqual(result, [0])

        # Test case 4: n = 10
        result = self.solution.countBits(10)
        self.assertEqual(result, [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2])

        # Test case 5: n = 15
        result = self.solution.countBits(15)
        self.assertEqual(result, [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4])

if __name__ == "__main__":
    unittest.main()
