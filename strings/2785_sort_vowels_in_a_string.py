import unittest

"""

Given a 0-indexed string s, permute s to get a new string t such that:

All consonants remain in their original places. More formally, if there is an index i with 0 <= i < s.length such that s[i] is a consonant, then t[i] = s[i].
The vowels must be sorted in the nondecreasing order of their ASCII values. More formally, for pairs of indices i, j with 0 <= i < j < s.length such that s[i] and s[j] are vowels, then t[i] must not have a higher ASCII value than t[j].
Return the resulting string.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in lowercase or uppercase. Consonants comprise all letters that are not vowels.

Constraints:

1 <= s.length <= 105
s consists only of letters of the English alphabet in uppercase and lowercase.

"""

class Solution:
    def sortVowels(self, s: str) -> str:

        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        vowels_found, places_found = [], []
        s = [l for l in s]

        for i, v in enumerate(s):
            if v in vowels:
                vowels_found.append(ord(v))
                places_found.append(i)

        vowels_found.sort()

        for i, v in enumerate(places_found):
            s[v] = chr(vowels_found[i])

        return "".join(s)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_sortVowels_emptyString(self):
        result = self.solution.sortVowels('')
        self.assertEqual(result, '')

    def test_sortVowels_noVowels(self):
        result = self.solution.sortVowels('xyz')
        self.assertEqual(result, 'xyz')

    def test_sortVowels_mixedCharacters(self):
        result = self.solution.sortVowels('Hello World')
        self.assertEqual(result, 'Hello World')

    def test_sortVowels_mixedCaseVowels(self):
        result = self.solution.sortVowels('aAEeIiOoUu')
        self.assertEqual(result, 'AEIOUaeiou')

    def test_sortVowels_repeatedVowels(self):
        result = self.solution.sortVowels('aabbccAAEE')
        self.assertEqual(result, 'AAbbccEEaa')


if __name__ == '__main__':
    unittest.main()
