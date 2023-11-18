import unittest
from typing import List

"""

The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
1 <= k <= 105

"""

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        nums = sorted(nums)
        l, r, = 0, 1
        curr_k, highest = 0, 1

        while r < len(nums):

            curr_k += ((r - l) * (nums[r] - nums[r - 1]))

            while curr_k > k:
                curr_k -= nums[r] - nums[l]
                l += 1

            highest = max((r + 1) - l, highest)
            r += 1

        return highest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maxFrequency_example1(self):
        nums = [1, 2, 4]
        k = 5
        result = self.solution.maxFrequency(nums, k)
        self.assertEqual(result, 3)  # Explanation: Replace 1 with 4, and the array becomes [4, 2, 4].

    def test_maxFrequency_example2(self):
        nums = [1, 4, 8, 13]
        k = 5
        result = self.solution.maxFrequency(nums, k)
        self.assertEqual(result, 2)  # Explanation: Replace 8 with 5, and the array becomes [1, 4, 5, 13].

    def test_maxFrequency_example3(self):
        nums = [3, 9, 6]
        k = 2
        result = self.solution.maxFrequency(nums, k)
        self.assertEqual(result, 1)  # Explanation: Replace 3 with 6, and the array becomes [6, 9, 6].


if __name__ == '__main__':
    unittest.main()
