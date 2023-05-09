import unittest

"""
Given a string s, find the length of the longest substring without repeating characters.

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s: return 0
        l, r, ret = 0, 1, 1

        while r < len(s):

            if s[r] in s[l:r]:
                pos = s[l:r].index(s[r])
                l += 1 + pos
                r += 1
            else:
                r += 1

            ret = max(ret, r - l)

        return ret



class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_lengthOfLongestSubstring_emptyString_returnsZero(self):
        result = self.solution.lengthOfLongestSubstring('')
        self.assertEqual(result, 0)

    def test_lengthOfLongestSubstring_singleCharacterString_returnsOne(self):
        result = self.solution.lengthOfLongestSubstring('a')
        self.assertEqual(result, 1)

    def test_lengthOfLongestSubstring_repeatedCharacterString_returnsOne(self):
        result = self.solution.lengthOfLongestSubstring('aaaaaa')
        self.assertEqual(result, 1)

    def test_lengthOfLongestSubstring_allDistinctCharactersString_returnsLength(self):
        result = self.solution.lengthOfLongestSubstring('abcdefg')
        self.assertEqual(result, 7)

    def test_lengthOfLongestSubstring_duplicateCharactersString_returnsLength(self):
        result = self.solution.lengthOfLongestSubstring('abcabcbb')
        self.assertEqual(result, 3)

    def test_lengthOfLongestSubstring_mixedCharactersString_returnsLength(self):
        result = self.solution.lengthOfLongestSubstring('pwwkew')
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
