import unittest
from typing import List
from collections import Counter

"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        count1 = Counter(nums1)
        ans = []

        for num in nums2:
            if count1[num] > 0:
                ans.append(num)
                count1[num] = 0

        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_intersection_empty_lists(self):
        nums1 = []
        nums2 = []
        result = self.solution.intersection(nums1, nums2)
        self.assertEqual(result, [])

    def test_intersection_no_common_elements(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        result = self.solution.intersection(nums1, nums2)
        self.assertEqual(result, [])

    def test_intersection_some_common_elements(self):
        nums1 = [1, 2, 2, 3, 4]
        nums2 = [2, 3, 3, 4, 5]
        result = self.solution.intersection(nums1, nums2)
        self.assertEqual(result, [2, 3, 4])

    def test_intersection_all_common_elements(self):
        nums1 = [1, 2, 3, 4, 5]
        nums2 = [1, 2, 3, 4, 5]
        result = self.solution.intersection(nums1, nums2)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_intersection_repeated_elements(self):
        nums1 = [1, 1, 2, 2, 3, 4]
        nums2 = [1, 2, 2, 3, 3, 4, 5]
        result = self.solution.intersection(nums1, nums2)
        self.assertEqual(result, [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
