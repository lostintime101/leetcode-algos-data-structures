import unittest

"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000

"""


class Solution:
    def rotate(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        if len(matrix) == 1: return

        l = 0
        r = len(matrix) - 1

        while l < r:

            top, bot = l, r

            for i in range(r - l):
                temp = matrix[top + i][r]

                matrix[top + i][r] = matrix[top][l + i]
                matrix[top][l + i] = matrix[bot - i][l]
                matrix[bot - i][l] = matrix[bot][r - i]
                matrix[bot][r - i] = temp

                # DOING SWAPS WITHOUT TEMP IS
                # A. CONFUSING AS HELL
                # B. INTRODUCES A BUG, 1 VALUE ALWAYS WRONG

                # matrix[top+i][r], \
                # matrix[bot][r-i], \
                # matrix[bot-i][l], \
                # matrix[top][l+i] = \
                # \
                # matrix[top][l+i], \
                # matrix[top-i][r], \
                # matrix[bot][r-i], \
                # matrix[bot-i][l]

            l += 1
            r -= 1


class TestRotate(unittest.TestCase):

    def test_empty_matrix(self):
        matrix = []
        Solution().rotate(matrix)
        self.assertEqual(matrix, [])

    def test_single_element_matrix(self):
        matrix = [[1]]
        Solution().rotate(matrix)
        self.assertEqual(matrix, [[1]])

    def test_2x2_matrix(self):
        matrix = [[1,2],[3,4]]
        Solution().rotate(matrix)
        self.assertEqual(matrix, [[3,1],[4,2]])

    def test_3x3_matrix(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        Solution().rotate(matrix)
        self.assertEqual(matrix, [[7,4,1],[8,5,2],[9,6,3]])

    def test_4x4_matrix(self):
        matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
        Solution().rotate(matrix)
        self.assertEqual(matrix, [[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]])


if __name__ == '__main__':
    unittest.main()

