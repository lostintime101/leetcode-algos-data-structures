import unittest

"""

You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

Return the score of s.

Constraints:

2 <= s.length <= 100
s consists only of lowercase English letters.

"""

class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        N = len(s)

        for i in range(N - 1):
            ans += abs(ord(s[i]) - ord(s[i + 1]))

        return ans


class TestScoreOfString(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_empty_string(self):
        self.assertEqual(self.solution.scoreOfString(""), 0)

    def test_single_character(self):
        self.assertEqual(self.solution.scoreOfString("a"), 0)

    def test_two_characters(self):
        self.assertEqual(self.solution.scoreOfString("ab"), 1)
        self.assertEqual(self.solution.scoreOfString("az"), 25)
        self.assertEqual(self.solution.scoreOfString("za"), 25)

    def test_multiple_characters(self):
        self.assertEqual(self.solution.scoreOfString("abc"), 2)
        self.assertEqual(self.solution.scoreOfString("hello"), 13)
        self.assertEqual(self.solution.scoreOfString("abcdef"), 5)
        self.assertEqual(self.solution.scoreOfString("zxy"), 3)

    def test_identical_characters(self):
        self.assertEqual(self.solution.scoreOfString("aaaa"), 0)

    def test_mixed_case(self):
        self.assertEqual(self.solution.scoreOfString("aA"), 32)
        self.assertEqual(self.solution.scoreOfString("aAzZ"), 121)


if __name__ == "__main__":
    unittest.main()
