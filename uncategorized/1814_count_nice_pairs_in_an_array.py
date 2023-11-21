import unittest
from typing import List
from collections import defaultdict

"""

You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:

0 <= i < j < nums.length
nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109

"""


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = (10 ** 9) + 7
        seen = defaultdict(int)

        for num in nums:
            rev = int(str(num)[::-1])
            seen[num - rev] += 1

        return sum([((val - 1) * (val)) // 2 for val in seen.values()]) % MOD


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_countNicePairs(self):
        # Test case 1
        nums1 = [42, 24, 12, 21]
        self.assertEqual(self.solution.countNicePairs(nums1), 0)

        # Test case 2
        nums2 = [123, 321, 555, 121]
        self.assertEqual(self.solution.countNicePairs(nums2), 1)

        # Test case 3
        nums3 = [111, 222, 333, 444]
        self.assertEqual(self.solution.countNicePairs(nums3), 6)


if __name__ == "__main__":
    unittest.main()
