import unittest

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

"""

class Solution:
    def longestCommonPrefix(self, strs) -> str:

        # 1: DOUBLE FOR LOOP

        # ret = strs[0]
        # if len(strs) == 1: return ret

        # for s in (range(1, len(strs))):

        #     word = strs[s]

        #     if len(word) < len(ret): ret = ret[:len(word)]

        #     for i in range(min(len(ret), len(word))):

        #         if ret[i] != word[i]:
        #             ret = ret[:i]
        #             break

        # return ret

        # 2: USING ZIP(*)

        a = list(zip(*strs))

        ret = ""
        for l in a:
            if len(set(l)) == 1:
                ret += l[0]
            else:
                return ret

        if ret: return ret
        return ""


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_double_for_loop(self):
        self.assertEqual(self.s.longestCommonPrefix(["flower","flow","flight"]), "fl")
        self.assertEqual(self.s.longestCommonPrefix(["dog","racecar","car"]), "")
        self.assertEqual(self.s.longestCommonPrefix(["ab","a"]), "a")
        self.assertEqual(self.s.longestCommonPrefix(["a"]), "a")

    def test_using_zip(self):
        self.assertEqual(self.s.longestCommonPrefix(["bracket","bright","brace"]), "br")
        self.assertEqual(self.s.longestCommonPrefix(["dog","racecar","car"]), "")
        self.assertEqual(self.s.longestCommonPrefix(["cdd","cd"]), "cd")
        self.assertEqual(self.s.longestCommonPrefix([""]), "")


if __name__ == '__main__':
    unittest.main()



