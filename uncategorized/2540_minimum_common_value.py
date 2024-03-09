import unittest
from typing import List

"""

Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

Constraints:

1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[j] <= 109
Both nums1 and nums2 are sorted in non-decreasing order.

"""

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        ans = -1
        a, b = 0, 0

        while a < len(nums1) and b < len(nums2):
            if nums1[a] == nums2[b]: return nums1[a]
            if nums1[a] < nums2[b]:
                a += 1
            else:
                b += 1

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_get_common(self):
        # Test case 1: Common element found in the middle
        nums1_1 = [1, 2, 3, 4, 5]
        nums2_1 = [0, 2, 6, 8, 9]
        self.assertEqual(self.solution.getCommon(nums1_1, nums2_1), 2)

        # Test case 2: Common element found at the beginning
        nums1_2 = [1, 3, 5, 7]
        nums2_2 = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.getCommon(nums1_2, nums2_2), 1)

        # Test case 3: No common element
        nums1_3 = [10, 20, 30]
        nums2_3 = [5, 15, 25]
        self.assertEqual(self.solution.getCommon(nums1_3, nums2_3), -1)

        # Test case 5: Common element found at the end
        nums1_5 = [1, 2, 3, 4]
        nums2_5 = [5, 6, 7, 8, 4]
        self.assertEqual(self.solution.getCommon(nums1_5, nums2_5), -1)


if __name__ == '__main__':
    unittest.main()
