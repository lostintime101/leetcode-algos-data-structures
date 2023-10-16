from typing import List
import unittest

"""

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

0 <= rowIndex <= 33

"""


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0: return [1]
        prev, row = [1], 0

        while True:
            row += 1
            curr = [1]
            for i in range(len(prev) - 1):
                curr.append(prev[i] + prev[i + 1])
            curr.append(1)
            prev = curr
            if row == rowIndex: return curr


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_row_0(self):
        self.assertEqual(self.solution.getRow(0), [1])

    def test_row_1(self):
        self.assertEqual(self.solution.getRow(1), [1, 1])

    def test_row_3(self):
        self.assertEqual(self.solution.getRow(3), [1, 3, 3, 1])

    def test_row_5(self):
        self.assertEqual(self.solution.getRow(5), [1, 5, 10, 10, 5, 1])

    def test_row_10(self):
        self.assertEqual(self.solution.getRow(10), [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1])


if __name__ == "__main__":
    unittest.main()
