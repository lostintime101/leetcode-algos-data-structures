import unittest
from typing import List

"""

Given an integer array nums, return the length of the longest strictly increasing 
subsequence.

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104

"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # DP SOLUTION

        # edge case
        if len(nums) == 1: return 1

        cache = [1 for num in nums]
        _max = 1

        for i in range(len(nums) - 2, -1, -1):

            for j in range(i + 1, len(nums)):

                if nums[i] < nums[j]:
                    cache[i] = max(cache[i], cache[j] + 1)
                    _max = max(cache[i], _max)

        return _max


class TestLengthOfLIS(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_length_of_lis_empty_list(self):
        nums = []
        self.assertEqual(self.solution.lengthOfLIS(nums), 1)

    def test_length_of_lis_single_element(self):
        nums = [5]
        self.assertEqual(self.solution.lengthOfLIS(nums), 1)

    def test_length_of_lis_no_increasing_subsequence(self):
        nums = [4, 3, 2, 1]
        self.assertEqual(self.solution.lengthOfLIS(nums), 1)

    def test_length_of_lis_sorted_sequence(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.lengthOfLIS(nums), 5)

    def test_length_of_lis_unsorted_sequence(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        self.assertEqual(self.solution.lengthOfLIS(nums), 4)

    def test_length_of_lis_duplicate_elements(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18, 101, 7]
        self.assertEqual(self.solution.lengthOfLIS(nums), 5)

    def test_length_of_lis_all_elements_same(self):
        nums = [5, 5, 5, 5, 5]
        self.assertEqual(self.solution.lengthOfLIS(nums), 1)


if __name__ == "__main__":
    unittest.main()
