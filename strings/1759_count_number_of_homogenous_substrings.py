import unittest

"""

Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 109 + 7.

A string is homogenous if all the characters of the string are the same.

A substring is a contiguous sequence of characters within a string.

Constraints:

1 <= s.length <= 105
s consists of lowercase letters.

"""

class Solution:
    def countHomogenous(self, s: str) -> int:

        MOD = 10 ** 9 + 7
        ret, count, prev = 0, 1, "A"

        for i in range(len(s)):

            if prev == s[i]:
                count += 1
            else:
                count = 1

            ret += count
            prev = s[i]

        return ret % MOD


class TestSolution(unittest.TestCase):
  def setUp(self):
      self.solution = Solution()

  def test_countHomogenous_1(self):
      s = "abbcccaaa"
      expected = 16
      self.assertEqual(self.solution.countHomogenous(s), expected)

  def test_countHomogenous_2(self):
      s = "abcabcabc"
      expected = 9
      self.assertEqual(self.solution.countHomogenous(s), expected)

  def test_countHomogenous_3(self):
      s = "aaaaaa"
      expected = 21
      self.assertEqual(self.solution.countHomogenous(s), expected)

  def test_countHomogenous_4(self):
      s = "abc"
      expected = 3
      self.assertEqual(self.solution.countHomogenous(s), expected)

  def test_countHomogenous_5(self):
      s = "a"
      expected = 1
      self.assertEqual(self.solution.countHomogenous(s), expected)


if __name__ == '__main__':
  unittest.main()



