import unittest
import heapq
from math import sqrt

"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, 
return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Constraints:

1 <= k <= points.length <= 104
-104 < xi, yi < 104

"""

class Solution:
    def kClosest(self, points: [[int]], k: int) -> [[int]]:

        # ZIP + SORT
        # dist = []
        # for point in points:
        #     dist.append(sqrt((point[0]**2) + (point[1]**2)))

        # a = sorted(list(zip(dist, points)))

        # return [i[1] for i in a[:k]]

        # MIN HEAP

        ret, stack = [], []
        dist = {}

        for point in points:

            d = sqrt((point[0] ** 2) + (point[1] ** 2))
            heapq.heappush(stack, d)

            if d in dist:
                dist[d].append(point)
            else:
                dist[d] = [point]

        while k > 0:

            d = heapq.heappop(stack)
            if dist[d]:
                ret.append(dist[d].pop())
                k -= 1

        return ret


class SolutionTests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_kClosest(self):
        points = [[1, 3], [-2, 2], [5, -1], [0, 0], [3, 4]]
        k = 2
        result = self.solution.kClosest(points, k)
        expected = [[0, 0], [-2, 2]]
        self.assertCountEqual(result, expected, "Incorrect result for test case 1")

        points = [[-1, 0], [2, 3], [-3, 4], [1, -1]]
        k = 3
        result = self.solution.kClosest(points, k)
        expected = [[-1, 0], [1, -1], [2, 3]]
        self.assertCountEqual(result, expected, "Incorrect result for test case 2")

        points = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        k = 1
        result = self.solution.kClosest(points, k)
        expected = [[0, 0]]
        self.assertCountEqual(result, expected, "Incorrect result for test case 3")

        points = [[-10, -10], [10, 10], [5, 5], [-5, -5]]
        k = 4
        result = self.solution.kClosest(points, k)
        expected = [[-5, -5], [5, 5], [-10, -10], [10, 10]]
        self.assertCountEqual(result, expected, "Incorrect result for test case 4")

if __name__ == "__main__":
    unittest.main()


if __name__ == "__main__":
    unittest.main()
