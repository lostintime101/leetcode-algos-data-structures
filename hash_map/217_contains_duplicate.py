import unittest
import collections

"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109

"""

class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:

        # 1 LINER, SETS METHOD
        # return len(set(nums)) != len(nums)

        # BASIC HASHMAP
        check = collections.defaultdict(list)

        for num in nums:
            if num in check: return True
            check[num] = 1
        return False


class TestContainsDuplicate(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_contains_duplicate_returns_true(self):
        nums = [1, 2, 3, 4, 5, 1]
        self.assertTrue(self.s.containsDuplicate(nums))

    def test_contains_duplicate_returns_false(self):
        nums = [1, 2, 3, 4, 5]
        self.assertFalse(self.s.containsDuplicate(nums))

    def test_contains_duplicate_empty_list(self):
        nums = []
        self.assertFalse(self.s.containsDuplicate(nums))

if __name__ == '__main__':
    unittest.main()
