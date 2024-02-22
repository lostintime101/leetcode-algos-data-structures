import unittest
from typing import List

"""

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

Constraints:

1 <= n <= 1000
0 <= trust.length <= 104
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n

"""


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        trusts = [0] * n
        is_trusted = [0] * n

        for t1, t2 in trust:
            trusts[t1 - 1] = 1
            is_trusted[t2 - 1] += 1

        for i in range(n):
            if trusts[i] == 0 and is_trusted[i] == n - 1:
                return i + 1

        return -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_find_judge_positive_case(self):
        n = 4
        trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
        result = self.solution.findJudge(n, trust)
        self.assertEqual(result, 3)

    def test_find_judge_negative_case(self):
        n = 3
        trust = [[1, 3], [2, 3]]
        result = self.solution.findJudge(n, trust)
        self.assertEqual(result, 3)

    def test_find_judge_single_person_case(self):
        n = 1
        trust = []
        result = self.solution.findJudge(n, trust)
        self.assertEqual(result, 1)

    def test_find_judge_empty_trust_case(self):
        n = 5
        trust = []
        result = self.solution.findJudge(n, trust)
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
