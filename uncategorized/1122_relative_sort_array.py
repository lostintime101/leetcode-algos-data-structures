import unittest
from typing import List
from collections import Counter

"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

Constraints:

1 <= arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
All the elements of arr2 are distinct.
Each arr2[i] is in arr1.

"""


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counts1 = Counter(arr1)
        ans = []

        for v in arr2:
            count = counts1[v]
            for i in range(count):
                ans.append(v)
            del counts1[v]

        end = []
        for k, v in counts1.items():
            for i in range(v):
                end.append(k)

        end = sorted(end)
        ans.extend(end)

        return ans


# Unit tests for the Solution class
class TestRelativeSortArray(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
        arr2 = [2, 1, 4, 3, 9, 6]
        expected = [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
        self.assertEqual(self.solution.relativeSortArray(arr1, arr2), expected)

    def test_case_2(self):
        arr1 = [28, 6, 22, 8, 44, 17]
        arr2 = [22, 28, 8, 6]
        expected = [22, 28, 8, 6, 17, 44]
        self.assertEqual(self.solution.relativeSortArray(arr1, arr2), expected)

    def test_case_3(self):
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [5, 4, 3, 2, 1]
        expected = [5, 4, 3, 2, 1]
        self.assertEqual(self.solution.relativeSortArray(arr1, arr2), expected)

    def test_case_4(self):
        arr1 = [4, 3, 4, 3, 2, 1, 2, 1]
        arr2 = [3, 2, 1]
        expected = [3, 3, 2, 2, 1, 1, 4, 4]
        self.assertEqual(self.solution.relativeSortArray(arr1, arr2), expected)

    def test_case_5(self):
        arr1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        arr2 = []
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(self.solution.relativeSortArray(arr1, arr2), expected)

    def test_case_6(self):
        arr1 = [10, 10, 10, 10]
        arr2 = [10]
        expected = [10, 10, 10, 10]
        self.assertEqual(self.solution.relativeSortArray(arr1, arr2), expected)

    def test_case_7(self):
        arr1 = [10, 20, 30]
        arr2 = [20, 10, 30]
        expected = [20, 10, 30]
        self.assertEqual(self.solution.relativeSortArray(arr1, arr2), expected)

    def test_case_8(self):
        arr1 = []
        arr2 = [1, 2, 3]
        expected = []
        self.assertEqual(self.solution.relativeSortArray(arr1, arr2), expected)


if __name__ == '__main__':
    unittest.main()
