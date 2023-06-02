import unittest
from typing import List

"""

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Constraints:

1 <= n <= 8

"""

class Solution:

    def __init__(self):
        self.ret = []

    def generateParenthesis(self, n: int) -> List[str]:

        stack = ""
        opening, closing = n, n
        self.dfs(stack, opening, closing)

        return self.ret

    def dfs(self, stack: str, op: int, cl: int) -> List[List[str]]:

        if not op and not cl:
            self.ret.append(stack)
            return

        if op:
            stack += "("
            op -= 1
            self.dfs(stack, op, cl)
            op += 1
            stack = stack[:-1]

        if cl > op:
            stack += ")"
            cl -= 1
            self.dfs(stack, op, cl)
            cl += 1
            stack = stack[:-1]



class TestSolution(unittest.TestCase):

    def test_generateParenthesis(self):
        solution = Solution()

        # Test case 1: n = 1
        n = 1
        expected = ["()"]
        self.assertTrue(all(p in solution.generateParenthesis(n) for p in expected))

        # Test case 2: n = 2
        n = 2
        expected = ["(())", "()()"]
        self.assertTrue(all(p in solution.generateParenthesis(n) for p in expected))

        # Test case 3: n = 3
        n = 3
        expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        self.assertTrue(all(p in solution.generateParenthesis(n) for p in expected))

        # Test case 4: n = 0
        n = 0
        expected = [""]
        self.assertTrue(all(p in solution.generateParenthesis(n) for p in expected))

if __name__ == '__main__':
    unittest.main()
