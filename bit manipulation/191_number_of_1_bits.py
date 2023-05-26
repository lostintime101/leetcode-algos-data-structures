import unittest

"""

Write a function that takes the binary representation of an unsigned integer 
and returns the number of '1' bits it has (also known as the Hamming weight).

Constraints:

The input must be a binary string of length 32.

"""

class Solution:
    def hammingWeight(self, n: int) -> int:

        # BIT MANIPULATION
        ret = 0
        while n:
            if n % 2 == 1:
                ret += 1
            n = n >> 1
        return ret

        # GOLFING SOLUTION
        return len([i for i in (bin(n)[2:]) if i == "1"])



class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = 0
        while n:
            if n % 2 == 1:
                ret += 1
            n = n >> 1
        return ret


class SolutionTestCase(unittest.TestCase):
    def test_hammingWeight(self):
        solution = Solution()

        # Test case: n = 11
        n = 11
        expected = 3
        self.assertEqual(solution.hammingWeight(n), expected)

        # Test case: n = 128
        n = 128
        expected = 1
        self.assertEqual(solution.hammingWeight(n), expected)

        # Test case: n = 0
        n = 0
        expected = 0
        self.assertEqual(solution.hammingWeight(n), expected)

        # Additional test cases
        # ...


if __name__ == '__main__':
    unittest.main()
