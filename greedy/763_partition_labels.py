import unittest
from collections import defaultdict

"""

You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.

"""


class Solution:
    def partitionLabels(self, s: str) -> [int]:

        # GREEDY (O)2n
        ret = []
        last = defaultdict()
        for i in range(len(s)): last[s[i]] = i

        localMax = last[s[0]]

        for i in range(len(s)):

            localMax = max(last[s[i]], localMax)

            if localMax == i:
                if len(ret): ret.append(i+1-sum(ret))
                else: ret.append(i+1)

        return ret

def test_partitionLabels():
    solution = Solution()

    # Test case 1
    s = "abac"
    expected_output = [3,1]
    assert solution.partitionLabels(s) == expected_output

    # Test case 2
    s = "abcdef"
    expected_output = [1, 1, 1, 1, 1, 1]
    assert solution.partitionLabels(s) == expected_output

    # Test case 3
    s = "aabbccddeeffgg"
    expected_output = [2, 2, 2, 2, 2, 2, 2]
    assert solution.partitionLabels(s) == expected_output

    # Test case 4
    s = "abcde"
    expected_output = [1, 1, 1, 1, 1]
    assert solution.partitionLabels(s) == expected_output

    # Test case 5 (single character)
    s = "a"
    expected_output = [1]
    assert solution.partitionLabels(s) == expected_output
    print("All test cases passed.")


test_partitionLabels()
