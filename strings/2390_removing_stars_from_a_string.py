import unittest

"""

You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters and stars *.
The operation above can be performed on s.

"""


class Solution:
    def removeStars(self, s: str) -> str:

        stack = []

        for l in s:
            if l == "*":
                stack.pop()
            else:
                stack.append(l)

        return "".join(stack)


class TestSolution(unittest.TestCase):
   def setUp(self):
       self.solution = Solution()

   def test_removeStars_1(self):
       s = "abc*def*"
       expected = "abde"
       self.assertEqual(self.solution.removeStars(s), expected)

   def test_removeStars_2(self):
       s = "abc*def*"
       expected = "abde"
       self.assertEqual(self.solution.removeStars(s), expected)

   def test_removeStars_3(self):
       s = "abc*def*ghi"
       expected = "abdeghi"
       self.assertEqual(self.solution.removeStars(s), expected)

   def test_removeStars_4(self):
       s = "abc*def*ghi*"
       expected = "abdegh"
       self.assertEqual(self.solution.removeStars(s), expected)


if __name__ == '__main__':
   unittest.main()
