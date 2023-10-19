import unittest

"""

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.

"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        new_s, new_t = [], []

        for i in range(len(s)):
            if s[i] == "#":
                if new_s: new_s.pop()
            else:
                new_s.append(s[i])

        for i in range(len(t)):
            if t[i] == "#":
                if new_t: new_t.pop()
            else:
                new_t.append(t[i])

        return new_s == new_t


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_backspaceCompare(self):
        self.assertTrue(self.solution.backspaceCompare("ab#c", "ad#c"))
        self.assertTrue(self.solution.backspaceCompare("ab##", "c#d#"))
        self.assertTrue(self.solution.backspaceCompare("a##c", "#a#c"))
        self.assertFalse(self.solution.backspaceCompare("a#c", "b"))
        self.assertFalse(self.solution.backspaceCompare("a", "aa"))


if __name__ == '__main__':
    unittest.main()
