import unittest

"""

For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.

"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if len(str1) >= len(str2):
            base, check = str1, str2
        else:
            base, check = str2, str1
        ret = ""

        for i in range(len(check)):
            curr = check[:i + 1]

            if (len(base) % len(curr)) or (len(check) % len(curr)): continue

            error_found = False
            for j in range(0, len(base), len(curr)):

                if (base[j:j + len(curr)] != curr) or (
                        ((j + len(curr)) <= len(check)) and (check[j:j + len(curr)] != curr)):
                    error_found = True
                    break

            if not error_found: ret = curr

        return ret


class SolutionTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_gcdOfStrings_example1(self):
        str1 = "ABCABC"
        str2 = "ABC"
        expected = "ABC"
        self.assertEqual(self.solution.gcdOfStrings(str1, str2), expected)

    def test_gcdOfStrings_example2(self):
        str1 = "ABABAB"
        str2 = "ABAB"
        expected = "AB"
        self.assertEqual(self.solution.gcdOfStrings(str1, str2), expected)

    def test_gcdOfStrings_example3(self):
        str1 = "LEET"
        str2 = "CODE"
        expected = ""
        self.assertEqual(self.solution.gcdOfStrings(str1, str2), expected)

    def test_gcdOfStrings_emptyStrings(self):
        str1 = ""
        str2 = ""
        expected = ""
        self.assertEqual(self.solution.gcdOfStrings(str1, str2), expected)

    def test_gcdOfStrings_sameStrings(self):
        str1 = "ABCD"
        str2 = "ABCD"
        expected = "ABCD"
        self.assertEqual(self.solution.gcdOfStrings(str1, str2), expected)

    def test_gcdOfStrings_noCommonSubstring(self):
        str1 = "XYZ"
        str2 = "ABC"
        expected = ""
        self.assertEqual(self.solution.gcdOfStrings(str1, str2), expected)


if __name__ == '__main__':
    unittest.main()
