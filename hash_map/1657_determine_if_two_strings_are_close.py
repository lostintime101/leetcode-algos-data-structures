import unittest
from collections import Counter

"""

Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

Constraints:

1 <= word1.length, word2.length <= 105
word1 and word2 contain only lowercase English letters.

"""

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        freq1 = Counter(word1)
        freq2 = Counter(word2)

        freq1_list, freq2_list = [], []
        letters1, letters2 = [], []

        for i,v in freq1.items():
            freq1_list.append(v)
            letters1.append(i)

        for i,val in freq2.items():
            freq2_list.append(val)
            letters2.append(i)

        return (sorted(freq1_list) == sorted(freq2_list)) and (set(letters1) == set(letters2))



# Unit tests
class TestSolution(unittest.TestCase):

    def test_closeStrings(self):
        # Test case 1: Empty strings
        solution = Solution()
        self.assertEqual(solution.closeStrings("", ""), True)

        # Test case 2: Strings with the same characters, but different frequencies
        solution = Solution()
        self.assertEqual(solution.closeStrings("abcde", "abcde"), True)

        # Test case 3: Strings with the same characters and frequencies, but different letters
        solution = Solution()
        self.assertEqual(solution.closeStrings("abc", "def"), False)

        # Test case 4: Strings with the same characters and frequencies, and same letters
        solution = Solution()
        self.assertEqual(solution.closeStrings("aabbbcc", "bccbbaa"), True)

        # Test case 5: Strings with different lengths
        solution = Solution()
        self.assertEqual(solution.closeStrings("abcd", "abc"), False)

if __name__ == '__main__':
    unittest.main()
