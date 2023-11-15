import unittest
from typing import List

"""
You are given an array of positive integers arr. Perform some operations (possibly none) on arr so that it satisfies these conditions:

The value of the first element in arr must be 1.
The absolute difference between any 2 adjacent elements must be less than or equal to 1. In other words, abs(arr[i] - arr[i - 1]) <= 1 for each i where 1 <= i < arr.length (0-indexed). abs(x) is the absolute value of x.
There are 2 types of operations that you can perform any number of times:

Decrease the value of any element of arr to a smaller positive integer.
Rearrange the elements of arr to be in any order.
Return the maximum possible value of an element in arr after performing the operations to satisfy the conditions.

Constraints:

1 <= arr.length <= 105
1 <= arr[i] <= 109

"""

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:

        arr = sorted(arr)
        arr[0] = 1

        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]: continue
            arr[i] = arr[i - 1] + 1

        return arr[-1]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case_1(self):
        arr = [2, 2, 1, 2, 1]
        result = self.solution.maximumElementAfterDecrementingAndRearranging(arr)
        self.assertEqual(result, 2)

    def test_example_case_2(self):
        arr = [100, 1, 1000]
        result = self.solution.maximumElementAfterDecrementingAndRearranging(arr)
        self.assertEqual(result, 3)

    def test_custom_case_1(self):
        arr = [1, 2, 3, 4, 5]
        result = self.solution.maximumElementAfterDecrementingAndRearranging(arr)
        self.assertEqual(result, 5)

    def test_custom_case_2(self):
        arr = [1, 2, 2, 3, 3, 3]
        result = self.solution.maximumElementAfterDecrementingAndRearranging(arr)
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
