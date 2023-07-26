import unittest

"""

You are given a string s consisting of only lowercase English letters. In one operation, you can do the following:

Select any non-empty substring of s, possibly the entire string, then replace each one of its characters with the previous character of the English alphabet. For example, 'b' is converted to 'a', and 'a' is converted to 'z'.
Return the lexicographically smallest string you can obtain after performing the above operation exactly once.

A substring is a contiguous sequence of characters in a string.

A string x is lexicographically smaller than a string y of the same length if x[i] comes before y[i] in alphabetic order for the first position i such that x[i] != y[i].

Constraints:

1 <= s.length <= 3 * 105
s consists of lowercase English letters

"""


class Solution:
    def smallestString(self, s: str) -> str:

        if set([l for l in s]) == set("a"):
            s = s[:-1]
            s += "z"
            return s

        ans = ""
        active = 0

        for l in s:
            if l != "a":
                if active == 0: active = 1
                if active != 2:
                    ans += chr(ord(l) - 1)
                else:
                    ans += l
            else:
                if active == 1: active = 2
                ans += "a"

        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_smallestString(self):
        # Test case with a string containing only 'a's
        s1 = "aaaa"
        expected1 = "aaaz"
        self.assertEqual(self.solution.smallestString(s1), expected1)

        # Test case with a string containing 'a's and other characters
        s2 = "abca"
        expected2 = "aaba"
        self.assertEqual(self.solution.smallestString(s2), expected2)

        # Test case with a string containing 'a's and other characters
        s3 = "xbcda"
        expected3 = "wabca"
        self.assertEqual(self.solution.smallestString(s3), expected3)

        # Test case with a single character 'a'
        s4 = "a"
        expected4 = "z"
        self.assertEqual(self.solution.smallestString(s4), expected4)

        # Test case with a single character 'z'
        s5 = "z"
        expected5 = "y"
        self.assertEqual(self.solution.smallestString(s5), expected5)

        # Test case with an empty string
        s6 = ""
        expected6 = ""
        self.assertEqual(self.solution.smallestString(s6), expected6)


if __name__ == '__main__':
    unittest.main()
