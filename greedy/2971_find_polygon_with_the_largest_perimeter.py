import unittest
from typing import List

"""
You are given an array of positive integers nums of length n.

A polygon is a closed plane figure that has at least 3 sides. The longest side of a polygon is smaller than the sum of its other sides.

Conversely, if you have k (k >= 3) positive real numbers a1, a2, a3, ..., ak where a1 <= a2 <= a3 <= ... <= ak and a1 + a2 + a3 + ... + ak-1 > ak, then there always exists a polygon with k sides whose lengths are a1, a2, a3, ..., ak.

The perimeter of a polygon is the sum of lengths of its sides.

Return the largest possible perimeter of a polygon whose sides can be formed from nums, or -1 if it is not possible to create a polygon.


Constraints:

3 <= n <= 105
1 <= nums[i] <= 109

"""

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        nums = sorted(nums)

        ans = -1
        count = nums[0] + nums[1]

        for i in range(2, len(nums)):

            if nums[i] < count:
                count += nums[i]
                ans = max(ans, count)
            else:
                count += nums[i]

        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_largestPerimeter(self):
        # Test case 1: Normal case
        nums1 = [2, 1, 2]
        self.assertEqual(self.solution.largestPerimeter(nums1), 5)

        # Test case 2: Normal case
        nums2 = [1, 2, 1]
        self.assertEqual(self.solution.largestPerimeter(nums2), -1)

        # Test case 3: Normal case
        nums3 = [3, 2, 3, 4]
        self.assertEqual(self.solution.largestPerimeter(nums3), 12)

        # Test case 4: All zeros
        nums4 = [0, 0, 0]
        self.assertEqual(self.solution.largestPerimeter(nums4), 0)

        # Test case 5: Random order
        nums5 = [5, 4, 2, 8]
        self.assertEqual(self.solution.largestPerimeter(nums5), 0)

        # Test case 6: Empty list
        nums6 = []
        self.assertEqual(self.solution.largestPerimeter(nums6), -1)


if __name__ == '__main__':
    unittest.main()
