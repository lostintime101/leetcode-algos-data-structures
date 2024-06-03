import unittest

"""

You are given two strings s and t consisting of only lowercase English letters.

Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

"""

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        N = len(s)
        M = len(t)
        point1, point2 = 0, 0

        while point1 < N and point2 < M:

            if s[point1] == t[point2]:
                point1 += 1
                point2 += 1
            else:
                point1 += 1

        return M - point2


class TestAppendCharacters(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_cases(self):
        # Test case 1: s and t are identical
        self.assertEqual(self.solution.appendCharacters("abc", "abc"), 0)

        # Test case 2: t is a substring of s
        self.assertEqual(self.solution.appendCharacters("abcdef", "ace"), 0)

        # Test case 3: t is not present in s at all
        self.assertEqual(self.solution.appendCharacters("abcdef", "xyz"), 3)

        # Test case 4: s is empty
        self.assertEqual(self.solution.appendCharacters("", "xyz"), 3)

        # Test case 5: t is empty
        self.assertEqual(self.solution.appendCharacters("abcdef", ""), 0)

        # Test case 6: s is shorter than t but has some matching characters
        self.assertEqual(self.solution.appendCharacters("ace", "abcdef"), 5)

        # Test case 7: s is much longer than t with t scattered within s
        self.assertEqual(self.solution.appendCharacters("abacadaeaf", "aaa"), 0)

        # Test case 8: All characters in t are in s but not in order
        self.assertEqual(self.solution.appendCharacters("abacadaeaf", "fa"), 1)

        # Test case 9: Partial match at the beginning of s
        self.assertEqual(self.solution.appendCharacters("abc", "abf"), 1)

        # Test case 10: Partial match at the end of s
        self.assertEqual(self.solution.appendCharacters("abcdef", "defg"), 1)


if __name__ == "__main__":
    unittest.main()
