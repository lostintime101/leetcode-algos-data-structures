import unittest
from typing import List
from collections import defaultdict

"""

There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

Constraints:

1 <= n <= 2 * 105
0 <= edges.length <= 2 * 105
edges[i].length == 2
0 <= ui, vi <= n - 1
ui != vi
0 <= source, destination <= n - 1
There are no duplicate edges.
There are no self edges.

"""

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        seen = [False] * n
        mapp = defaultdict(list)

        for [a, b] in edges:
            mapp[a].append(b)
            mapp[b].append(a)

        prev = [source]
        curr = []

        while prev:

            for p in prev:
                if p == destination:
                    return True

                if seen[p]:
                    continue
                else:
                    seen[p] = True

                curr.extend(mapp[p])

            prev = curr
            curr = []

        return False


class TestSolution(unittest.TestCase):
    def test_valid_path(self):
        solution = Solution()

        # Test case 1: Single edge graph with source and destination connected
        edges1 = [[0, 1]]
        self.assertTrue(solution.validPath(2, edges1, 0, 1))

        # Test case 2: Single edge graph with source and destination not connected
        edges2 = [[0, 1]]
        self.assertFalse(solution.validPath(2, edges2, 0, 2))

        # Test case 3: Disconnected graph
        edges3 = [[0, 1], [2, 3], [4, 5]]
        self.assertFalse(solution.validPath(6, edges3, 0, 5))

        # Test case 4: Connected graph with multiple paths
        edges4 = [[0, 1], [1, 2], [2, 3], [3, 4], [0, 5], [5, 4]]
        self.assertTrue(solution.validPath(6, edges4, 0, 4))

        # Test case 5: Graph with cycles
        edges5 = [[0, 1], [1, 2], [2, 0]]
        self.assertTrue(solution.validPath(3, edges5, 0, 2))


if __name__ == '__main__':
    unittest.main()
