import unittest
from typing import List

"""

You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106
1 <= k <= 105

"""

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        N = len(nums)
        mx = max(nums)
        count, ans, start = 0, 0, 0

        for end in range(N):
            if nums[end] == mx:
                count += 1

            while count >= k and start <= end:
                ans += N - end
                if nums[start] == mx:
                    count -= 1
                start += 1

        return ans


class TestSolution(unittest.TestCase):
    def test_countSubarrays(self):
        solution = Solution()

        # Test case 1
        nums1 = [1, 2, 3, 4, 5]
        k1 = 2
        self.assertEqual(solution.countSubarrays(nums1, k1), 0)

        # Test case 2
        nums2 = [1, 2, 2, 2, 1]
        k2 = 2
        self.assertEqual(solution.countSubarrays(nums2, k2), 8)

        # Test case 3
        nums3 = [2, 2, 2, 2, 2]
        k3 = 1
        self.assertEqual(solution.countSubarrays(nums3, k3), 15)

        # Test case 4
        nums4 = [3, 3, 3, 3, 3]
        k4 = 3
        self.assertEqual(solution.countSubarrays(nums4, k4), 6)

        # Test case 5
        nums5 = [1, 2, 3, 4, 5]
        k5 = 1
        self.assertEqual(solution.countSubarrays(nums5, k5), 5)


if __name__ == '__main__':
    unittest.main()
