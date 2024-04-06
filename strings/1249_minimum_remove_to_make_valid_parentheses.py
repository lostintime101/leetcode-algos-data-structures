import unittest


"""

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

Constraints:

1 <= s.length <= 105
s[i] is either'(' , ')', or lowercase English letter.

"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        ends, opened = 0, 0
        ans = ""

        for l in s:
            if l == ")": ends += 1

        for l in s:

            if l == "(":
                if ends == 0:
                    continue
                else:
                    ends -= 1
                    opened += 1

            if l == ")":
                if opened > 0:
                    opened -= 1
                else:
                    ends -= 1
                    continue

            ans += l

        return ans


class TestSolution(unittest.TestCase):
    def test_minRemoveToMakeValid(self):
        solution = Solution()

        # Test case with balanced parentheses
        self.assertEqual(solution.minRemoveToMakeValid("()"), "()")

        # Test case with unbalanced parentheses at the end
        self.assertEqual(solution.minRemoveToMakeValid("())"), "()")

        # Test case with unbalanced parentheses at the beginning
        self.assertEqual(solution.minRemoveToMakeValid("(()"), "()")

        # Test case with unbalanced parentheses in the middle
        self.assertEqual(solution.minRemoveToMakeValid("(a(b)c)d"), "(a(b)c)d")

        # Test case with no parentheses
        self.assertEqual(solution.minRemoveToMakeValid("abc"), "abc")

        # Test case with nested parentheses
        self.assertEqual(solution.minRemoveToMakeValid("a(b(c)d)e(f(g)h)i)"), "a(b(c)d)e(f(g)h)i")

        # Test case with multiple unbalanced parentheses
        self.assertEqual(solution.minRemoveToMakeValid("))(("), "")

        # Test case with empty string
        self.assertEqual(solution.minRemoveToMakeValid(""), "")


if __name__ == "__main__":
    unittest.main()
