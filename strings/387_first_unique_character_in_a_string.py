import unittest

"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.

"""

class Solution:
    def firstUniqChar(self, s: str) -> int:

        seen = []
        seen_once = {}

        for i, v in enumerate(s):
            if v not in seen:
                seen.append(v)
                seen_once[v] = i
            else:
                if v in seen_once: del seen_once[v]

        if seen_once: return min(seen_once.values())
        return -1


class TestSolution(unittest.TestCase):

    def test_firstUniqChar(self):
        sol = Solution()

        # Test case 1
        s = "leetcode"
        self.assertEqual(sol.firstUniqChar(s), 0)

        # Test case 2
        s = "loveleetcode"
        self.assertEqual(sol.firstUniqChar(s), 2)

        # Test case 3
        s = "aabbcc"
        self.assertEqual(sol.firstUniqChar(s), -1)

        # Test case 4
        s = ""
        self.assertEqual(sol.firstUniqChar(s), -1)


if __name__ == '__main__':
    unittest.main()
