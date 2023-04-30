import unittest
import collections

"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # SORT FUNCTION
        return sorted(s) == sorted(t)

        # HASH MAP

        check = collections.defaultdict(list)

        for i in s: check[i] = 1
        for i in t:
            if not check[i]:
                return False
            else:
                check[i] -= 1
        return True


class TestSolution(unittest.TestCase):

    def test_isAnagram(self):
        solution = Solution()

        # Test case 1
        s1 = "anagram"
        t1 = "nagaram"
        expected_output1 = True
        self.assertEqual(solution.isAnagram(s1, t1), expected_output1)

        # Test case 2
        s2 = "rat"
        t2 = "car"
        expected_output2 = False
        self.assertEqual(solution.isAnagram(s2, t2), expected_output2)

        # Test case 3
        s3 = ""
        t3 = ""
        expected_output3 = True
        self.assertEqual(solution.isAnagram(s3, t3), expected_output3)

        # Test case 4
        s4 = "a"
        t4 = "a"
        expected_output4 = True
        self.assertEqual(solution.isAnagram(s4, t4), expected_output4)

        # Test case 5
        s5 = "abcdefg"
        t5 = "gfedcba"
        expected_output5 = True
        self.assertEqual(solution.isAnagram(s5, t5), expected_output5)


if __name__ == '__main__':
    unittest.main()
