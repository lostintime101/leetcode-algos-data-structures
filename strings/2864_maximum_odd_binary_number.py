import unittest

"""

You are given a binary string s that contains at least one '1'.

You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.

Return a string representing the maximum odd binary number that can be created from the given combination.

Note that the resulting string can have leading zeros.

Constraints:

1 <= s.length <= 100
s consists only of '0' and '1'.
s contains at least one '1'.

"""


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:

        ones = s.count("1")

        return ("1" * (ones-1)) + ("0" * (len(s) - ones)) + "1"


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        input_str = "110101"
        output_str = self.solution.maximumOddBinaryNumber(input_str)
        self.assertEqual(output_str, "111001")

    def test_all_zeros(self):
        input_str = "000001"
        output_str = self.solution.maximumOddBinaryNumber(input_str)
        self.assertEqual(output_str, "000001")

    def test_all_ones(self):
        input_str = "111111"
        output_str = self.solution.maximumOddBinaryNumber(input_str)
        self.assertEqual(output_str, "111111")

    def test_mixed_ones_and_zeros(self):
        input_str = "101010"
        output_str = self.solution.maximumOddBinaryNumber(input_str)
        self.assertEqual(output_str, "110001")


if __name__ == "__main__":
    unittest.main()
