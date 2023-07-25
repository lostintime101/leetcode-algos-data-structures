import unittest
from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for word in words:
            word = word.split(separator)
            for w in word:
                if w:
                    ans.append(w)
        return ans


class TestSolution(unittest.TestCase):

    def test_splitWordsBySeparator_single_separator(self):
        sol = Solution()
        words = ["hello-world", "python-is-awesome", "unittests-are-cool"]
        separator = "-"
        expected_result = ["hello", "world", "python", "is", "awesome", "unittests", "are", "cool"]
        result = sol.splitWordsBySeparator(words, separator)
        self.assertEqual(result, expected_result)

    def test_splitWordsBySeparator_multiple_separators(self):
        sol = Solution()
        words = ["apple|banana|orange", "dog|cat|mouse", "one|two|three"]
        separator = "|"
        expected_result = ["apple", "banana", "orange", "dog", "cat", "mouse", "one", "two", "three"]
        result = sol.splitWordsBySeparator(words, separator)
        self.assertEqual(result, expected_result)

    def test_splitWordsBySeparator_no_separator(self):
        sol = Solution()
        words = ["hello", "world", "python", "is", "awesome"]
        separator = "-"
        expected_result = ["hello", "world", "python", "is", "awesome"]
        result = sol.splitWordsBySeparator(words, separator)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
