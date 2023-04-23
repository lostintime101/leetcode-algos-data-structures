import unittest

"""
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

        # EXAMPLES + LOGIC
        # A A (26 + 1)
        # ret = 27

        # Z Z (26^2 + 26^1)
        # ret = 702

        # A A A (26*26*1 + 26*1 + 1)
        # ret = 703

        # Z Z Z (26^3 + 26^2 + 26^1)
        # ret = 18278

        # Z B Y (26^3 * (26 * 2) + 1 * 25)
        # ret = 17653

Constraints:

1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].

"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alpha = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
                 "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
                 "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18,
                 "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24,
                 "Y": 25, "Z": 26}

        ret = 0

        for i, c in enumerate(columnTitle[::-1]):
            level = 26 ** i
            ret += level * alpha[c]

        return ret


class TestTitleToNumber(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_single_column(self):
        self.assertEqual(self.s.titleToNumber("A"), 1)
        self.assertEqual(self.s.titleToNumber("B"), 2)
        self.assertEqual(self.s.titleToNumber("Z"), 26)

    def test_multiple_columns(self):
        self.assertEqual(self.s.titleToNumber("AA"), 27)
        self.assertEqual(self.s.titleToNumber("AB"), 28)
        self.assertEqual(self.s.titleToNumber("AZ"), 52)
        self.assertEqual(self.s.titleToNumber("BA"), 53)
        self.assertEqual(self.s.titleToNumber("ZZ"), 702)
        self.assertEqual(self.s.titleToNumber("AAA"), 703)
        self.assertEqual(self.s.titleToNumber("AAB"), 704)
        self.assertEqual(self.s.titleToNumber("ABC"), 731)
        self.assertEqual(self.s.titleToNumber("ZZZ"), 18278)


if __name__ == '__main__':
    unittest.main()
