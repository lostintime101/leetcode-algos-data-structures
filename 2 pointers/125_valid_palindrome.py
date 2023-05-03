import unittest

"""

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing
all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

"""


class Solution:
    def isPalindrome(self, s: str) -> bool:

        # foo = "".join([i for i in s.lower() if i.isalpha() or i.isnumeric()])

        # return foo[::-1] == foo

        # 2 POINTERS METHOD

        s = s.lower()
        ss = ""

        for i in range(len(s)):
            if not s[i].isalpha() and not s[i].isnumeric():
                continue
            else:
                ss += s[i]

        l, r = 0, len(ss) - 1

        while l <= r:
            if ss[l] != ss[r]: return False
            l += 1
            r -= 1

        return True


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        s = "A man, a plan, a canal: Panama"
        expected = True
        self.assertEqual(self.solution.isPalindrome(s), expected)

    def test_2(self):
        s = "race a car"
        expected = False
        self.assertEqual(self.solution.isPalindrome(s), expected)

    def test_3(self):
        s = "Was it a car or a cat I saw?"
        expected = True
        self.assertEqual(self.solution.isPalindrome(s), expected)

    def test_4(self):
        s = "No 'x' in Nixon"
        expected = True
        self.assertEqual(self.solution.isPalindrome(s), expected)

    def test_5(self):
        s = "12321"
        expected = True
        self.assertEqual(self.solution.isPalindrome(s), expected)

    def test_6(self):
        s = "1a2"
        expected = False
        self.assertEqual(self.solution.isPalindrome(s), expected)

    def test_7(self):
        s = ""
        expected = True
        self.assertEqual(self.solution.isPalindrome(s), expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
