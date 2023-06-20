import unittest
from typing import List

"""

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.

"""
class Node:
    def __init__(self, val: int, prereqs):
        self.val = val
        self.pre = prereqs


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        courses = [Node(i, []) for i in range(numCourses)]
        for preq in prerequisites: courses[preq[0]].pre.append(courses[preq[1]])
        loop = [0]

        def dfs(visited, pre, cked):

            for c in pre:
                if c in cked: continue
                if c in visited:
                    loop[0] = 1
                    break
                visited[c] = 1
                dfs(visited, c.pre, cked)
                del visited[c]
                cked.add(c)

        checked = set()
        for course in courses:
            dfs({course: 1}, course.pre, checked)
            if loop[0] == 1:
                return False
            else:
                checked.add(course)

        return True


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_canFinish(self):
        # Test case with no prerequisites
        prerequisites1 = []
        self.assertTrue(self.solution.canFinish(3, prerequisites1))

        # Test case with a valid course order
        prerequisites2 = [[1, 0], [2, 1]]
        self.assertTrue(self.solution.canFinish(3, prerequisites2))

        # Test case with cyclic dependencies
        prerequisites3 = [[1, 0], [0, 1]]
        self.assertFalse(self.solution.canFinish(2, prerequisites3))

        # Test case with multiple prerequisites for a course
        prerequisites4 = [[1, 0], [2, 0], [3, 1], [3, 2]]
        self.assertTrue(self.solution.canFinish(4, prerequisites4))

if __name__ == '__main__':
    unittest.main()
