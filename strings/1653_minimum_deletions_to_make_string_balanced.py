import unittest

"""

You are given a string s consisting only of characters 'a' and 'b'​​​​.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.

Constraints:

1 <= s.length <= 105
s[i] is 'a' or 'b'​​.

"""

class Solution:
    def minimumDeletions(self, s: str) -> int:

        N = len(s)
        a_count, b_count = 0, 0

        for l in s:
            if l == "a":
                a_count += 1
            else:
                b_count += 1

        ans = a_count

        a_front, b_front = 0, 0

        for i in range(N):
            if s[i] == "a":
                a_count -= 1
                a_front += 1
            if s[i] == "b":
                b_count -= 1
                b_front += 1

            ans = min(ans, a_count + b_front)

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_all_a(self):
        self.assertEqual(self.solution.minimumDeletions("aaa"), 0)

    def test_all_b(self):
        self.assertEqual(self.solution.minimumDeletions("bbb"), 0)

    def test_mixed_ab(self):
        self.assertEqual(self.solution.minimumDeletions("abab"), 1)
        self.assertEqual(self.solution.minimumDeletions("aabbab"), 1)
        self.assertEqual(self.solution.minimumDeletions("bbaaabbb"), 2)

    def test_edge_cases(self):
        self.assertEqual(self.solution.minimumDeletions(""), 0)
        self.assertEqual(self.solution.minimumDeletions("a"), 0)
        self.assertEqual(self.solution.minimumDeletions("b"), 0)
        self.assertEqual(self.solution.minimumDeletions("ab"), 0)
        self.assertEqual(self.solution.minimumDeletions("ba"), 1)


if __name__ == "__main__":
    unittest.main()
