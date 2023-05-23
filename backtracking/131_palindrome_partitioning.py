import unittest

"""

Given a string s, partition s such that every 
substring of the partition is a palindrome. 
Return all possible palindrome partitioning of s.

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.

"""

class Solution:
    def partition(self, s: str) -> [[str]]:

        ret = []
        left, right = 0, 0

        def isPalindrome(string):
            if len(string) == 0: return False
            if string[::-1] == string: return True
            return False

        def findSubstrings(substrings, l, r):

            if l > len(s) - 1:
                ret.append(substrings.copy())
                return

            while r <= len(s):

                if isPalindrome(s[l:r]):
                    substrings.append(s[l:r])
                    templ = l
                    l = r
                    findSubstrings(substrings, l, r)
                    substrings.pop()
                    l, r = templ, r + 1
                else:
                    r += 1

            l += 1

        findSubstrings([], left, right)

        return ret



class SolutionTests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_partition_palindrome(self):
        s = "aab"
        expected = [['a', 'a', 'b'], ['aa', 'b']]
        result = self.solution.partition(s)
        self.assertEqual(result, expected)

    def test_partition_single_character(self):
        s = "a"
        expected = [['a']]
        result = self.solution.partition(s)
        self.assertEqual(result, expected)

    def test_partition_empty_string(self):
        s = ""
        expected = [[]]
        result = self.solution.partition(s)
        self.assertEqual(result, expected)

    def test_partition_non_palindrome(self):
        s = "abc"
        expected = [['a', 'b', 'c']]
        result = self.solution.partition(s)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
