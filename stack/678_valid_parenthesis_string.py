import unittest

"""

Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

Constraints:

1 <= s.length <= 100
s[i] is '(', ')' or '*'.

"""

class Solution:
    def checkValidString(self, s: str) -> bool:

        # STACK

        stack, wildCards = [], []

        for i, v in enumerate(s):
            if v == "(":
                stack.append(i)
            elif v == "*":
                wildCards.append(i)
            else:
                if len(stack) > 0:
                    stack.pop()
                elif len(wildCards) > 0:
                    wildCards.pop()
                else:
                    return False

        # wildCards only valid if before the "(", early wildcards can't help later in the stack
        while stack and wildCards:
            if wildCards[-1] > stack[-1]:
                wildCards.pop()
                stack.pop()
            else:
                return False

        return not stack



class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_valid_strings(self):
        self.assertTrue(self.solution.checkValidString("()"))  # Valid string
        self.assertTrue(self.solution.checkValidString("(*)"))  # Valid string
        self.assertTrue(self.solution.checkValidString("(*))"))  # Valid string
        self.assertTrue(self.solution.checkValidString("((*)"))  # Valid string
        self.assertTrue(self.solution.checkValidString("()**"))  # Valid string

    def test_invalid_strings(self):
        self.assertFalse(self.solution.checkValidString("("))  # Invalid string
        self.assertFalse(self.solution.checkValidString(")"))  # Invalid string
        self.assertFalse(self.solution.checkValidString(")*"))  # Invalid string
        self.assertFalse(self.solution.checkValidString(")*("))  # Invalid string
        self.assertFalse(self.solution.checkValidString("(*))("))  # Invalid string

    def test_empty_string(self):
        self.assertTrue(self.solution.checkValidString(""))  # Empty string is valid

if __name__ == '__main__':
    unittest.main()
