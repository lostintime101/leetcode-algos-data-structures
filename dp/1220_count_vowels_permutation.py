import unittest

"""

Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.

Constraints:

1 <= n <= 2 * 10^4

"""

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 1_000_000_007
        ans = 5
        curr = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}
        new = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

        for _ in range(1, n):
            new["a"] += (curr["u"] + curr["i"] + curr["e"])
            new["e"] += (curr["a"] + curr["i"])
            new["i"] += (curr["o"] + curr["e"])
            new["o"] += curr["i"]
            new["u"] += (curr["o"] + curr["i"])

            curr = new
            new = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

        return sum(curr.values()) % MOD


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        self.assertEqual(self.solution.countVowelPermutation(1), 5)

    def test_case_2(self):
        self.assertEqual(self.solution.countVowelPermutation(2), 10)

    def test_case_3(self):
        self.assertEqual(self.solution.countVowelPermutation(5), 68)

    def test_case_4(self):
        self.assertEqual(self.solution.countVowelPermutation(10), 1739)

    def test_case_5(self):
        self.assertEqual(self.solution.countVowelPermutation(25), 29599477)

    def test_case_6(self):
        self.assertEqual(self.solution.countVowelPermutation(50), 227130014)


if __name__ == "__main__":
    unittest.main()
