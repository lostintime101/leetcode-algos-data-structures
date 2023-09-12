import unittest

"""

A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

Constraints:

1 <= s.length <= 105
s contains only lowercase English letters.

"""

class Solution:
    def minDeletions(self, s: str) -> int:

        # FREQ MAPPING SOLUTION
        # ans = 0
        # freq = Counter(s)
        # freq2 = defaultdict(int)
        # for k,v in freq.items(): freq2[v] += 1

        # found = True

        # while found:
        #     found = False

        #     for k,v in freq2.items():

        #         if k and v > 1:
        #             freq2[k] -= 1
        #             ans += 1
        #             found = True
        #             break

        #     freq2[k-1] += 1

        # return ans

        # GREEDY SOLUTION
        freq = [0] * 26

        for c in s:
            freq[ord(c) - ord("a")] += 1
        ans = 0

        freq = sorted(freq, reverse=True)

        for i in range(len(freq) - 1):

            if freq[i + 1] == 0: break

            while freq[i] <= freq[i + 1]:
                freq[i + 1] -= 1
                ans += 1
                if freq[i + 1] == 0: break

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minDeletions(self):
        # Test cases
        self.assertEqual(self.solution.minDeletions("aab"), 0)
        self.assertEqual(self.solution.minDeletions("abcabc"), 3)
        self.assertEqual(self.solution.minDeletions("aaabbbccc"), 3)
        self.assertEqual(self.solution.minDeletions("abcdefg"), 6)
        self.assertEqual(self.solution.minDeletions("aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz"), 49)
        self.assertEqual(self.solution.minDeletions(""), 0)


if __name__ == "__main__":
    unittest.main()
