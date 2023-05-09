import unittest

"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length

"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l, r, ret = 0, 1, 1
        window = {s[l]: 1}

        while r < len(s):

            # if s[r] in window: window[s[r]] += 1
            # else: window[s[r]] = 1

            window[s[r]] = 1 + window.get(s[r], 0)

            maxi, total = 0, 0
            for i, v in window.items():
                total += v
                maxi = max(maxi, v)

            while k < (total - maxi):
                window[s[l]] -= 1
                total -= 1
                l += 1

            ret = max(total, ret)
            r += 1

        return ret


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_characterReplacement_singleCharacterString_returnsOne(self):
        result = self.solution.characterReplacement('a', 2)
        self.assertEqual(result, 1)

    def test_characterReplacement_allSameCharacterString_returnsLength(self):
        result = self.solution.characterReplacement('aaaaa', 2)
        self.assertEqual(result, 5)

    def test_characterReplacement_replaceAllCharactersString_returnsLength(self):
        result = self.solution.characterReplacement('abcde', 5)
        self.assertEqual(result, 5)

    def test_characterReplacement_replaceSomeCharactersString_returnsLength(self):
        result = self.solution.characterReplacement('aabbaabb', 1)
        self.assertEqual(result, 3)

    def test_characterReplacement_mixedCharactersString_returnsLength(self):
        result = self.solution.characterReplacement('ABAB', 2)
        self.assertEqual(result, 4)

    def test_characterReplacement_kGreaterThanStringLength_returnsLength(self):
        result = self.solution.characterReplacement('abcd', 5)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()
