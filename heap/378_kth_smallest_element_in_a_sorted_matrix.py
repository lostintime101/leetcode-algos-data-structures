import unittest

"""

Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2

"""


class Solution:
    def kthSmallest(self, matrix, k: int) -> int:

        # HEAPIFY SOLUTION

        # final = matrix[0]

        # heapq.heapify(final)

        # for v in matrix[1:]:

        #     for value in v: heapq.heappush(final, value)

        # for _ in range(k-1): heapq.heappop(final)

        # return heapq.heappop(final)

        # STANDARD SORT FUNCTION SOLUTION

        final = []

        for row in matrix:
            for v in row:
                final.append(v)

        return sorted(final)[k - 1]


class TestKthSmallest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_sort_function_solution(self):
        matrix = [
            [1, 5, 9],
            [10, 11, 13],
            [12, 13, 15]
        ]
        self.assertEqual(self.s.kthSmallest(matrix, 8), 13)

        matrix = [
            [-5]
        ]
        self.assertEqual(self.s.kthSmallest(matrix, 1), -5)

        matrix = [
            [1, 2],
            [1, 3]
        ]
        self.assertEqual(self.s.kthSmallest(matrix, 2), 1)


if __name__ == '__main__':
    unittest.main()



