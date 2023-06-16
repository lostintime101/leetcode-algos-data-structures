import unittest
from typing import List
from collections import defaultdict

"""

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.

"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordDict = set(wordDict)
        wordMap = defaultdict(dict)

        for word in wordDict:
            level = wordMap
            for letter in word:
                if not level[letter]: level[letter] = defaultdict(dict)
                level = level[letter]

        pointers = {0}

        for i in range(1, len(s)):

            newPointers = []
            for p in pointers:
                if s[p:i] in wordDict:
                    newPointers.append(i)

            for p in newPointers:
                pointers.add(i)

            removePointers = []
            for p in pointers:
                word = s[p:i]
                start = wordMap
                for l in word:
                    if not start[l]: removePointers.append(p)
                    start = start[l]

            for p in removePointers: pointers.remove(p)

        for p in pointers:
            if s[p:] in wordDict:
                return True

        return False


import unittest
from collections import defaultdict
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        wordMap = defaultdict(dict)

        for word in wordDict:
            level = wordMap
            for letter in word:
                if not level[letter]:
                    level[letter] = defaultdict(dict)
                level = level[letter]

        pointers = {0}

        for i in range(1, len(s)):
            newPointers = []
            for p in pointers:
                if s[p:i] in wordDict:
                    newPointers.append(i)

            for p in newPointers:
                pointers.add(i)

            removePointers = []
            for p in pointers:
                word = s[p:i]
                start = wordMap
                for l in word:
                    if not start[l]:
                        removePointers.append(p)
                    start = start[l]

            for p in removePointers:
                pointers.remove(p)

        for p in pointers:
            if s[p:] in wordDict:
                return True

        return False


class SolutionTests(unittest.TestCase):
    def test_wordBreak(self):
        solution = Solution()

        # Test case 1: The string "leetcode" can be segmented into ["leet", "code"]
        self.assertTrue(solution.wordBreak("leetcode", ["leet", "code"]))

        # Test case 2: The string "applepenapple" can be segmented into ["apple", "pen", "apple"]
        self.assertTrue(solution.wordBreak("applepenapple", ["apple", "pen"]))

        # Test case 3: The string "catsandog" cannot be segmented into valid words
        self.assertFalse(solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))

        # Test case 4: The string "aaaaaaa" can be segmented into ["aaa", "aaa", "a"]
        self.assertTrue(solution.wordBreak("aaaaaaa", ["aaa", "a"]))

    def test_wordBreak_empty_wordDict(self):
        solution = Solution()

        # Test case 6: Non-empty string cannot be segmented with an empty wordDict
        self.assertFalse(solution.wordBreak("leetcode", []))

    def test_wordBreak_single_letter_words(self):
        solution = Solution()

        # Test case 7: The string "abcd" can be segmented into ["a", "b", "c", "d"]
        self.assertTrue(solution.wordBreak("abcd", ["a", "b", "c", "d"]))

    def test_wordBreak_single_letter_wordDict(self):
        solution = Solution()

        # Test case 8: The string "abcd" cannot be segmented with a single-letter wordDict
        self.assertFalse(solution.wordBreak("abcd", ["x"]))

if __name__ == '__main__':
    unittest.main()
