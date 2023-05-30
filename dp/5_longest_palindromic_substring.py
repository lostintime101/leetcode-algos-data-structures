import unittest
import collections

"""

Given a string s, return the longest palindromic substring in s.

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

"""

class Solution:
    def longestPalindrome(self, s: str) -> str:

        ans = ""
        substrings = collections.defaultdict()

        for i, v in enumerate(s):
            if v in substrings:
                substrings[v].append(i)
            else:
                substrings[v] = [i]

        for substring in substrings.values():
            for i in range(len(substring)):
                L = substring[i]
                for j in range(len(substring) - 1, i - 1, -1):
                    R = substring[j]
                    if s[L:R + 1] == s[L:R + 1][::-1]:
                        if len(s[L:R + 1]) > len(ans): ans = s[L:R + 1]
                        break

        return ans

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
        # ret = s[0]

        # for i in range(len(s)):

        #     l, r = i, i

        #     while (l >= 0) and (r < len(s)) and s[l] == s[r]:

        #         if (r - l + 1) > len(ret):
        #             ret = s[l:r+1]

        #         l -= 1
        #         r += 1

        #     l, r = i, i+1

        #     while (l >= 0) and (r < len(s)) and s[l] == s[r]:

        #         if (r - l + 1) > len(ret):
        #             ret = s[l:r+1]

        #         l -= 1
        #         r += 1

        # return ret


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_character(self):
        # Single character string should be a palindrome
        s = "a"
        expected = "a"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, expected)

    def test_no_palindrome(self):
        # No palindrome in the string
        s = "xyz"
        expected = "x"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, expected)

    def test_even_length_palindrome(self):
        # Even length palindrome
        s = "babad"
        expected = "bab"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, expected)

    def test_odd_length_palindrome(self):
        # Odd length palindrome
        s = "cbbd"
        expected = "bb"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, expected)

    def test_multiple_palindromes(self):
        # Multiple palindromes in the string
        s = "abccbaabcdedcba"
        expected = "abcdedcba"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()

