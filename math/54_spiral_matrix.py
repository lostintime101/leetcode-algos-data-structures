import unittest
from typing import List

"""

Given an m x n matrix, return all elements of the matrix in spiral order.

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []

        while len(matrix) > 0:
            # add top row to answer
            ret.extend(matrix[0])

            # cut top row
            matrix = matrix[1:]

            # rotate matrix counter-clockwise
            matrix = list(zip(*matrix))[::-1]

        return ret


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_spiralOrder(self):
        matrix1 = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]
        self.assertEqual(self.solution.spiralOrder(matrix1), [1, 2, 3, 6, 9, 8, 7, 4, 5])

        matrix2 = [[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]]
        self.assertEqual(self.solution.spiralOrder(matrix2), [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])

        matrix3 = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [10, 11, 12]]
        self.assertEqual(self.solution.spiralOrder(matrix3), [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8])

        matrix4 = [[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10]]
        self.assertEqual(self.solution.spiralOrder(matrix4), [1, 2, 3, 4, 5, 10, 9, 8, 7, 6])

if __name__ == '__main__':
    unittest.main()
