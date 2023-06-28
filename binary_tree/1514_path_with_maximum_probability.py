import unittest
from typing import List
from collections import defaultdict
from math import isclose
"""

You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

Constraints:

2 <= n <= 10^4
0 <= start, end < n
start != end
0 <= a, b < n
a != b
0 <= succProb.length == edges.length <= 2*10^4
0 <= succProb[i] <= 1
There is at most one edge between every two nodes.


"""


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

        edges_sorted = defaultdict(list)

        for i in range(len(edges)):
            edges_sorted[edges[i][0]].append((edges[i], succProb[i]))
            edges_sorted[edges[i][1]].append((edges[i][::-1], succProb[i]))

        prev, curr = [start], []
        high = defaultdict(float)
        high[start] = float(1)

        # BFS
        while prev:

            for node in prev:
                for edge in edges_sorted[node]:
                    destination = edge[0][1]
                    prob = high[node] * edge[1]

                    if high[destination] < prob:
                        curr.append(destination)
                        high[destination] = prob

            prev = curr
            curr = []

        return high[end]
    