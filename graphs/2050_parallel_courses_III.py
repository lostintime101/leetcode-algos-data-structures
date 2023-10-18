import unittest
from collections import defaultdict
from typing import List

"""

You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given a 2D integer array relations where relations[j] = [prevCoursej, nextCoursej] denotes that course prevCoursej has to be completed before course nextCoursej (prerequisite relationship). Furthermore, you are given a 0-indexed integer array time where time[i] denotes how many months it takes to complete the (i+1)th course.

You must find the minimum number of months needed to complete all the courses following these rules:

You may start taking a course at any time if the prerequisites are met.
Any number of courses can be taken at the same time.
Return the minimum number of months needed to complete all the courses.

Note: The test cases are generated such that it is possible to complete every course (i.e., the graph is a directed acyclic graph).

Constraints:

1 <= n <= 5 * 104
0 <= relations.length <= min(n * (n - 1) / 2, 5 * 104)
relations[j].length == 2
1 <= prevCoursej, nextCoursej <= n
prevCoursej != nextCoursej
All the pairs [prevCoursej, nextCoursej] are unique.
time.length == n
1 <= time[i] <= 104
The given graph is a directed acyclic graph.


"""

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:

        starts = defaultdict(list)
        requirements = defaultdict(list)

        for fr, to in relations:
            requirements[to].append(fr)
            starts[fr].append(to)

        # print(starts, requirements)

        prev = []
        for i in range(1, n + 1):
            if not requirements.get(i): prev.append(i)

        t = [max(time)]

        seen = {}

        def bfs(node, curr_t):

            if node in seen:
                if curr_t > seen[node]:
                    seen[node] = curr_t
                else:
                    return
            else:
                seen[node] = curr_t

            if not starts.get(node):
                t[0] = max(t[0], curr_t)
                return

            for next_node in starts[node]:
                bfs(next_node, curr_t + time[next_node - 1])

        for p in prev:
            bfs(p, time[p - 1])

        return t[0]


class TestMinimumTime(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case_1(self):
        n = 5
        relations = [[1, 2], [1, 3], [2, 4], [2, 5]]
        time = [3, 2, 4, 5, 1]
        result = self.solution.minimumTime(n, relations, time)
        self.assertEqual(result, 10)

    def test_example_case_2(self):
        n = 3
        relations = [[1, 2], [1, 3]]
        time = [2, 3, 4]
        result = self.solution.minimumTime(n, relations, time)
        self.assertEqual(result, 6)

    def test_empty_relations(self):
        n = 3
        relations = []
        time = [2, 3, 4]
        result = self.solution.minimumTime(n, relations, time)
        self.assertEqual(result, 4)

    def test_single_node(self):
        n = 1
        relations = []
        time = [5]
        result = self.solution.minimumTime(n, relations, time)
        self.assertEqual(result, 5)

    def test_large_input(self):
        n = 100
        relations = [[i, i+1] for i in range(1, 100)]
        time = [i for i in range(1, 101)]
        result = self.solution.minimumTime(n, relations, time)
        self.assertEqual(result, 5050)


if __name__ == "__main__":
    unittest.main()
