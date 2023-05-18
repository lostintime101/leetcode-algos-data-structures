
"""
Given a directed acyclic graph, with n vertices numbered from 0 to n-1, 
and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

Find the smallest set of vertices from which all nodes in the graph are reachable. 
It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.

Constraints:

2 <= n <= 10^5
1 <= edges.length <= min(10^5, n * (n - 1) / 2)
edges[i].length == 2
0 <= fromi, toi < n
All pairs (fromi, toi) are distinct.

"""

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: [[int]]) -> [int]:
        # SETS BRUTE FORCE
        starts, ends, ret = set(), set(), []

        for edge in edges:
            starts.add(edge[0])
            ends.add(edge[1])

        return [start for start in starts if start not in ends]


def test_findSmallestSetOfVertices():
    solution = Solution()

    # Test case 1
    n = 6
    edges = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
    expected_output = [0, 3]
    assert solution.findSmallestSetOfVertices(n, edges) == expected_output

    # Test case 2
    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    expected_output = [0]
    assert solution.findSmallestSetOfVertices(n, edges) == expected_output

    # Test case 4 (single edge)
    n = 3
    edges = [[0, 1]]
    expected_output = [0]
    assert solution.findSmallestSetOfVertices(n, edges) == expected_output

    print("All test cases passed.")


test_findSmallestSetOfVertices()
