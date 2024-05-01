import unittest

"""
Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
Return the resulting string.

Constraints:

1 <= word.length <= 250
word consists of lowercase English letters.
ch is a lowercase English letter.

"""

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        for i, l in enumerate(word):
            if l == ch:
                return word[:i + 1][::-1] + word[i + 1:]

        return word


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_reversePrefix(self):
        self.assertEqual(self.solution.reversePrefix("example", "a"), "axemple")
        self.assertEqual(self.solution.reversePrefix("hello", "o"), "olleh")
        self.assertEqual(self.solution.reversePrefix("world", "d"), "dlrow")

    def test_reversePrefix_no_prefix(self):
        # Test when the character ch is not found in the word
        self.assertEqual(self.solution.reversePrefix("example", "z"), "example")
        self.assertEqual(self.solution.reversePrefix("hello", "x"), "hello")
        self.assertEqual(self.solution.reversePrefix("world", "z"), "world")


if __name__ == '__main__':
    unittest.main()