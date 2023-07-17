import unittest

"""

A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1" 'B' -> "2" ... 'Z' -> "26" To decode an encoded message, all the digits must be grouped then mapped back 
into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped 
into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).

"""


class Solution:

    def numDecodings(self, s: str) -> int:

        cache = {-1: 0, 1: 1}

        if s[0] in ["1", "2"]:
            cache[-1] = 1
        elif s[0] == "0":
            return 0

        for i, v in enumerate(s):

            if (v == "0") and (i != 0):
                if s[i - 1] not in ["1", "2"]: return 0
                cache[i] = cache[i - 2]
                continue

            if i == 0:
                cache[i] = 1
            else:
                cache[i] = cache[i - 1]

            if (i > 0) and ((s[i - 1] == "1") or (s[i - 1] == "2" and int(s[i]) < 7)):
                cache[i] += cache[i - 2]

        return cache[len(s) - 1]


class SolutionTests(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_numDecodings(self):
        # Test cases with expected outputs
        self.assertEqual(self.solution.numDecodings("12"), 2)
        self.assertEqual(self.solution.numDecodings("226"), 3)
        self.assertEqual(self.solution.numDecodings("0"), 0)
        self.assertEqual(self.solution.numDecodings("06"), 0)
        self.assertEqual(self.solution.numDecodings("10"), 1)
        self.assertEqual(self.solution.numDecodings("101"), 1)
        self.assertEqual(self.solution.numDecodings("27"), 1)
        self.assertEqual(self.solution.numDecodings("0"), 0)
        self.assertEqual(self.solution.numDecodings("123456789"), 3)
        self.assertEqual(self.solution.numDecodings("2611055971756562"), 4)

        # Additional test case
        self.assertEqual(self.solution.numDecodings("11111"), 8)  # All characters are 1


if __name__ == '__main__':
    unittest.main()
