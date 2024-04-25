import unittest

"""
You are given a string s consisting of lowercase letters and an integer k. We call a string t ideal if the following conditions are satisfied:

t is a subsequence of the string s.
The absolute difference in the alphabet order of every two adjacent letters in t is less than or equal to k.
Return the length of the longest ideal string.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

Note that the alphabet order is not cyclic. For example, the absolute difference in the alphabet order of 'a' and 'z' is 25, not 1.

Constraints:

1 <= s.length <= 105
0 <= k <= 25
s consists of lowercase English letters.

"""

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        alpha = [0] * 26

        for l in s:
            curr = ord(l) - 97
            low = max(0, curr - k)
            high = min(26, curr + k)

            alpha[curr] = max(alpha[low:high + 1])
            alpha[curr] += 1

        return max(alpha)


class TestSolution(unittest.TestCase):
    def test_longest_ideal_string(self):
        solution = Solution()

        # Test case 1: Regular case
        s1 = "abcde"
        k1 = 5
        self.assertEqual(solution.longestIdealString(s1, k1), 5)

        # Test case 2: All characters are the same
        s2 = "aaaaa"
        k2 = 1
        self.assertEqual(solution.longestIdealString(s2, k2), 5)

        # Test case 3: Empty string
        s3 = ""
        k3 = 3
        self.assertEqual(solution.longestIdealString(s3, k3), 0)

        # Test case 4: Larger string
        s4 = "abcdefghijklmnopqrstuvwxyz"
        k4 = 6
        self.assertEqual(solution.longestIdealString(s4, k4), 26)

        # Test case 5: Edge case with single character
        s5 = "a"
        k5 = 1
        self.assertEqual(solution.longestIdealString(s5, k5), 1)


if __name__ == "__main__":
    unittest.main()
