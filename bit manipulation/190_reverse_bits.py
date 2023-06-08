import unittest

"""

Reverse bits of a given 32 bits unsigned integer.

Constraints:

The input must be a binary string of length 32

"""

class Solution:
    def reverseBits(self, n: int) -> int:

        return int((format(n, '032b')[::-1]), 2)


        # ALT ANS
        # ret = 0

        # for i in range(32):
        #     bit = n >>i & 1
        #     ret += bit << (31-i)
        # return ret


class Solution:
    def reverseBits(self, n: int) -> int:
        return int((format(n, '032b')[::-1]), 2)

class SolutionTests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_reverseBits_example1(self):
        result = self.solution.reverseBits(43261596)
        self.assertEqual(result, 964176192)

    def test_reverseBits_example2(self):
        result = self.solution.reverseBits(4294967293)
        self.assertEqual(result, 3221225471)

    def test_reverseBits_zero(self):
        result = self.solution.reverseBits(0)
        self.assertEqual(result, 0)

    def test_reverseBits_max_value(self):
        result = self.solution.reverseBits(4294967295)
        self.assertEqual(result, 4294967295)

    def test_reverseBits_min_value(self):
        result = self.solution.reverseBits(1)
        self.assertEqual(result, 2147483648)

if __name__ == '__main__':
    unittest.main()

