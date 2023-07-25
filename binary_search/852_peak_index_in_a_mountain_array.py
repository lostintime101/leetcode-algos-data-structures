import unittest
from typing import List

"""

An array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity.

Constraints:

3 <= arr.length <= 105
0 <= arr[i] <= 106
arr is guaranteed to be a mountain array.

"""


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr)-1
        while l <= r:
            mid = (l+r) // 2
            if mid == 0: mid = 1
            if mid == len(arr)-1: mid = len(arr)-2
            if arr[mid-1] < arr[mid] > arr[mid+1]: return mid
            if arr[mid-1] < arr[mid] < arr[mid+1]: l = mid+1
            if arr[mid-1] > arr[mid] > arr[mid+1]: r = mid-1
        return mid

class TestSolution(unittest.TestCase):

    def test_peakIndexInMountainArray_peak_at_middle(self):
        sol = Solution()
        arr = [1, 3, 5, 4, 2]
        expected_result = 2
        result = sol.peakIndexInMountainArray(arr)
        self.assertEqual(result, expected_result)

    def test_peakIndexInMountainArray_peak_at_beginning(self):
        sol = Solution()
        arr = [3, 5, 2, 1]
        expected_result = 1
        result = sol.peakIndexInMountainArray(arr)
        self.assertEqual(result, expected_result)

    def test_peakIndexInMountainArray_peak_at_end(self):
        sol = Solution()
        arr = [1, 3, 5, 7, 9, 8]
        expected_result = 4
        result = sol.peakIndexInMountainArray(arr)
        self.assertEqual(result, expected_result)

    def test_peakIndexInMountainArray_single_element(self):
        sol = Solution()
        arr = [1, 10, 4]
        expected_result = 1
        result = sol.peakIndexInMountainArray(arr)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
