import unittest
from functools import cache

"""

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m 
substrings
 respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.

"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3): return False
        ans = [False]

        @cache
        def backtrack(p1, p2, p3):

            if p3 == len(s3):
                ans[0] = True
                return

            if (p1 < len(s1)) and (s1[p1] == s3[p3]): backtrack(p1 + 1, p2, p3 + 1)
            if (p2 < len(s2)) and (s2[p2] == s3[p3]): backtrack(p1, p2 + 1, p3 + 1)

        backtrack(0, 0, 0)

        return ans[0]


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_interleave_positive(self):
        self.assertTrue(self.solution.isInterleave("abc", "def", "adbcef"))

    def test_interleave_negative(self):
        self.assertFalse(self.solution.isInterleave("abc", "def", "abcdefg"))

    def test_interleave_empty_strings(self):
        self.assertTrue(self.solution.isInterleave("", "", ""))

    def test_interleave_one_empty_string(self):
        self.assertTrue(self.solution.isInterleave("", "abc", "abc"))
        self.assertTrue(self.solution.isInterleave("abc", "", "abc"))
        self.assertFalse(self.solution.isInterleave("abc", "", "ab"))

    def test_interleave_repeated_chars(self):
        self.assertTrue(self.solution.isInterleave("aaa", "bbb", "ababab"))
        self.assertFalse(self.solution.isInterleave("aaa", "bbb", "abababa"))

    def test_interleave_long_strings(self):
        self.assertTrue(self.solution.isInterleave(
            "a" * 100, "b" * 100, "ab" * 100))
        self.assertFalse(self.solution.isInterleave(
            "a" * 100, "b" * 100, "a" * 100 + "b" * 99))


if __name__ == '__main__':
    unittest.main()

