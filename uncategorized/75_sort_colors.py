import unittest

"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Constraints:

0 <= num <= 231 - 1
"""

class Solution:
    def addDigits(self, num: int) -> int:

        # STRING METHOD

        # while num > 9: num = sum([int(n) for n in str(num)])

        # return num

        # INTS METHOD

        while num > 9:
            sum = 0

            while num:
                sum += num % 10
                num = num // 10

            num = sum

        return num


class TestSolution(unittest.TestCase):

    def test_addDigits(self):
        s = Solution()

        # Test case 1
        num = 38
        expected_output = 2
        self.assertEqual(s.addDigits(num), expected_output)

        # Test case 2
        num = 0
        expected_output = 0
        self.assertEqual(s.addDigits(num), expected_output)

        # Test case 3
        num = 123456789
        expected_output = 9
        self.assertEqual(s.addDigits(num), expected_output)

        # Test case 4
        num = 1111111111
        expected_output = 1
        self.assertEqual(s.addDigits(num), expected_output)

        # Test case 5
        num = 987654321
        expected_output = 9
        self.assertEqual(s.addDigits(num), expected_output)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
