import unittest
from typing import List

"""

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 
Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

"""

class Solution:

    def evalRPN(self, tokens: List[str]) -> int:

        ops = ("+", "-", "*", "/")
        numStack = []
        tokens = tokens[::-1]

        while tokens:
            operation = ""

            if tokens[-1] not in ops:
                numStack.append(tokens[-1])
            else:
                operation = tokens[-1]

            tokens.pop()

            if operation:
                a = int(numStack.pop())
                b = int(numStack.pop())

                if operation == "+":
                    b += a
                elif operation == "-":
                    b -= a
                elif operation == "*":
                    b *= a
                else:
                    b = int(b / a)
                numStack.append(str(b))

        return int(numStack[0])


class TestSolution(unittest.TestCase):

    def test_evalRPN(self):
        solution = Solution()

        # Test case 1: Addition
        tokens = ["2", "1", "+", "3", "*"]
        self.assertEqual(solution.evalRPN(tokens), 9)

        # Test case 2: Subtraction
        tokens = ["4", "13", "5", "/", "+"]
        self.assertEqual(solution.evalRPN(tokens), 6)

        # Test case 3: Multiplication
        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        self.assertEqual(solution.evalRPN(tokens), 22)

        # Test case 4: Division
        tokens = ["3", "4", "+"]
        self.assertEqual(solution.evalRPN(tokens), 7)

        # Test case 5: Complex expression
        tokens = ["4", "5", "7", "*", "+", "3", "-"]
        self.assertEqual(solution.evalRPN(tokens), 36)

if __name__ == '__main__':
    unittest.main()
