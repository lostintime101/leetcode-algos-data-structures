import unittest
from typing import List
from collections import defaultdict

"""

You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100

"""

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        mx = 0
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
            mx = max(mx, counts[num])

        ans = 0
        for count in counts.values():
            if count == mx:
                ans += mx

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_max_frequency_elements(self):
        # Test case 1
        nums1 = [1, 2, 2, 3, 3, 3]
        self.assertEqual(self.solution.maxFrequencyElements(nums1), 3)

        # Test case 2
        nums2 = [4, 4, 4, 5, 5, 6]
        self.assertEqual(self.solution.maxFrequencyElements(nums2), 3)

        # Test case 3
        nums3 = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.maxFrequencyElements(nums3), 5)

        # Test case 4
        nums4 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        self.assertEqual(self.solution.maxFrequencyElements(nums4), 10)


if __name__ == '__main__':
    unittest.main()
