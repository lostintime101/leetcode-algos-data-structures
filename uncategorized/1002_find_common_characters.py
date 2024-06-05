import unittest
from typing import List

"""

Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.

"""


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        N = len(words)
        prev = [0] * 26

        for l in words[0]:
            l = ord(l) - ord("a")
            prev[l] += 1

        for i in range(1, N):
            curr = [0] * 26

            for l in words[i]:
                l = ord(l) - ord("a")
                if prev[l] > 0:
                    curr[l] += 1
                    prev[l] -= 1

            prev = curr

        ans = []

        for i in range(26):
            while prev[i] > 0:
                ans.append(chr(i + 97))
                prev[i] -= 1

        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_common_chars_1(self):
        words = ["bella", "label", "roller"]
        expected = ["e", "l", "l"]
        result = self.solution.commonChars(words)
        self.assertCountEqual(result, expected)  # Use assertCountEqual for lists where order doesn't matter

    def test_common_chars_2(self):
        words = ["cool", "lock", "cook"]
        expected = ["c", "o"]
        result = self.solution.commonChars(words)
        self.assertCountEqual(result, expected)

    def test_common_chars_3(self):
        words = ["hello", "world", "python"]
        expected = ["o"]
        result = self.solution.commonChars(words)
        self.assertCountEqual(result, expected)


if __name__ == '__main__':
    unittest.main()