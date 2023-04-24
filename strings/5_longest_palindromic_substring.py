import unittest

"""
Given a string s, return the longest palindromic substring in s.

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:

        # # BRUTE FORCE OPTIMIZED
        # ret = s[0]

        # for start in range(len(s)):
        #     ss = s[start:]
        #     l = len(ss)-1

        #     # optimization 1
        #     if len(ret) >= len(ss): return ret

        #     # optimization 2 (start from end)
        #     for ii in range(len(ss)-1, -1, -1):

        #         sss = ss[:ii+1]

        #         if sss == sss[::-1]:
        #             if len(ret) < len(sss): ret = sss

        # return ret

        # CHECK OUTWARDS METHOD
        ret = s[0]

        for i in range(len(s)):

            l, r = i, i

            while (l >= 0) and (r < len(s)) and s[l] == s[r]:

                if (r - l + 1) > len(ret):
                    ret = s[l:r + 1]

                l -= 1
                r += 1

            l, r = i, i + 1

            while (l >= 0) and (r < len(s)) and s[l] == s[r]:

                if (r - l + 1) > len(ret):
                    ret = s[l:r + 1]

                l -= 1
                r += 1

        return ret


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_longestPalindrome(self):
        self.assertEqual(self.solution.longestPalindrome("babad"), "bab")
        self.assertEqual(self.solution.longestPalindrome("cbbd"), "bb")
        self.assertEqual(self.solution.longestPalindrome("a"), "a")
        self.assertEqual(self.solution.longestPalindrome("ac"), "a")
        self.assertEqual(self.solution.longestPalindrome("aaaa"), "aaaa")
        self.assertEqual(self.solution.longestPalindrome("abcda"), "a")
        self.assertEqual(self.solution.longestPalindrome("abbbbbba"), "abbbbbba")


if __name__ == '__main__':
    unittest.main()


