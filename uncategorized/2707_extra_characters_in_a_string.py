import unittest
from functools import cache
from typing import List

"""

You are given a 0-indexed string s and a dictionary of words dictionary. 
You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. 
There may be some extra characters in s which are not present in any of the substrings.

Return the minimum number of extra characters left over if you break up s optimally.

Constraints:

1 <= s.length <= 50
1 <= dictionary.length <= 50
1 <= dictionary[i].length <= 50
dictionary[i] and s consists of only lowercase English letters
dictionary contains distinct words

"""


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        ans = [len(s)]

        @cache
        def backtrack(curr, unused):

            if curr > len(s):
                return
            elif curr == len(s):
                ans[0] = min(ans[0], unused)
                return

            for word in dictionary:

                if len(word) > len(s) - curr: continue

                match = True
                for i in range(len(word)):
                    if word[i] != s[curr + i]:
                        match = False
                        break

                if match: backtrack(curr + len(word), unused)

            backtrack(curr + 1, unused + 1)

        backtrack(0, 0)

        return ans[0]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minExtraChar(self):
        # Test with a simple case
        s = "abcdef"
        dictionary = ["abc", "def"]
        self.assertEqual(self.solution.minExtraChar(s, dictionary), 0)

        # Test with a case where extra characters are needed
        s = "abcdef"
        dictionary = ["ab", "cd", "efg"]
        self.assertEqual(self.solution.minExtraChar(s, dictionary), 2)

        # Test with an empty string
        s = ""
        dictionary = ["abc", "def"]
        self.assertEqual(self.solution.minExtraChar(s, dictionary), 0)

        # Test with an empty dictionary
        s = "abcdef"
        dictionary = []
        self.assertEqual(self.solution.minExtraChar(s, dictionary), 6)

        # Test with a case where no dictionary words match
        s = "abcdef"
        dictionary = ["xyz", "123"]
        self.assertEqual(self.solution.minExtraChar(s, dictionary), 6)


if __name__ == '__main__':
    unittest.main()
