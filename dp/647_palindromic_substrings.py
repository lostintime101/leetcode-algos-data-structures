import unittest
from collections import defaultdict

"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.

"""

class Solution:
    def countSubstrings(self, s: str) -> int:

        ret = 0
        hashmap = defaultdict()

        for i, v in enumerate(s):
            if v in hashmap:
                hashmap[v].append(i)
            else:
                hashmap[v] = [i]

        for substrings in hashmap.values():

            for i in range(len(substrings)):
                L = substrings[i]

                for j in range(i, len(substrings)):
                    R = substrings[j]
                    if s[L:R + 1] == s[L:R + 1][::-1]: ret += 1

        return ret


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_string(self):
        # Empty string should have no substrings
        s = ""
        expected = 0
        result = self.solution.countSubstrings(s)
        self.assertEqual(result, expected)

    def test_single_character(self):
        # Single character string is a palindrome
        s = "a"
        expected = 1
        result = self.solution.countSubstrings(s)
        self.assertEqual(result, expected)

    def test_no_palindrome(self):
        # No palindrome in the string
        s = "xyz"
        expected = 3  # Substrings: 'x', 'y', 'z'
        result = self.solution.countSubstrings(s)
        self.assertEqual(result, expected)

    def test_palindromes(self):
        # Palindromes in the string
        s = "abcba"
        expected = 7  # Substrings: 'a', 'b', 'c', 'b', 'a', 'abcba', 'bcb'
        result = self.solution.countSubstrings(s)
        self.assertEqual(result, expected)

    def test_duplicate_characters(self):
        # String with duplicate characters
        s = "aaa"
        expected = 6  # Substrings: 'a', 'a', 'a', 'aa', 'aa', 'aaa'
        result = self.solution.countSubstrings(s)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
