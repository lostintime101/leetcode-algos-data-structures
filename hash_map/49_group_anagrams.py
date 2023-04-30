import unittest
import collections
from typing import List

"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # DOESN'T WORK FOR EDGE CASE ["a","a"]

        # ret = []
        # words = {}

        # def letters(word):
        #     hashmap = collections.defaultdict(dict)
        #     for l in word:
        #         if hashmap[l]:
        #             hashmap[l] += 1
        #         else:
        #             hashmap[l] = 1
        #     return [hashmap]

        # for i in range(len(strs)):
        #     words[strs[i]] = letters(strs[i])

        # print(words)

        # while strs:
        #     curr = strs[-1]
        #     strs.pop(-1)

        #     if curr in words:
        #         word = words[curr]
        #     else: continue

        #     group = []

        #     for i,v in words.items():
        #         if v == word:
        #             group.append(i)

        #     for i in group:
        #         del words[i]

        #     ret.append(group)

        # return ret

        # HASHMAP VERSION 2
        keys = collections.defaultdict(list)

        for word in strs:

            counts = [0 for i in range(26)]

            for i in word:
                counts[ord(i) - ord("a")] += 1

            # THIS CAN CREATE BUG FOR [0,1,0,10] AND [0,1,0,1,0]
            # strcounts = "".join([str(num) for num in counts])

            # CAST TO TUPLE RESOLVES BUG
            keys[tuple(counts)].append(word)

        return keys.values()


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_groupAnagrams(self):
        test_cases = [
            (["eat", "tea", "tan", "ate", "nat", "bat"], [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]),
            ([""], [[""]]),
            (["a"], [["a"]]),
            (["a", "a"], [["a", "a"]]),
            (["listen", "silent", "abc", "cba"], [["listen", "silent"], ["abc", "cba"]])
        ]
        for strs, expected in test_cases:
            with self.subTest(strs=strs, expected=expected):
                result = self.solution.groupAnagrams(strs)
                # sort the sublists for easy comparison
                result = [sorted(r) for r in result]
                expected = [sorted(e) for e in expected]
                # sort the main list to not consider order
                result.sort()
                expected.sort()
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
