import unittest

"""

Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.

"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        for i in range(len(s) // 2):

            if len(s) % (i + 1): continue

            substring = s[:i + 1]

            substring *= int(len(s) / len(substring))

            if substring == s: return True

        return False


class TestSolution(unittest.TestCase):

    def test_repeatedSubstringPattern(self):
        solution = Solution()

        # Test cases with repeated substring patterns
        self.assertTrue(solution.repeatedSubstringPattern("abcabcabc"))
        self.assertTrue(solution.repeatedSubstringPattern("aaaaaa"))
        self.assertTrue(solution.repeatedSubstringPattern("abababab"))

        # Test cases with non-repeated substring patterns
        self.assertFalse(solution.repeatedSubstringPattern("abcdef"))
        self.assertFalse(solution.repeatedSubstringPattern("abcabcabcbbc"))
        self.assertFalse(solution.repeatedSubstringPattern("aabbcc"))

        # Edge cases
        self.assertFalse(solution.repeatedSubstringPattern("a"))
        self.assertTrue(solution.repeatedSubstringPattern("aa"))
        self.assertTrue(solution.repeatedSubstringPattern("aaa"))


if __name__ == '__main__':
    unittest.main()
