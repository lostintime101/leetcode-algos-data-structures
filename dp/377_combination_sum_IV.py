import unittest
from typing import List

"""

Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 1000
All the elements of nums are unique.
1 <= target <= 1000

"""


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        dp = {0: 1}

        for i in range(1, target + 1):
            dp[i] = 0
            for num in nums:
                dp[i] += dp.get(i - num, 0)

        return dp[target]


class TestCombinationSum4(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 2, 3]
        target = 4
        self.assertEqual(self.solution.combinationSum4(nums, target), 7)

    def test_example_2(self):
        nums = [9]
        target = 3
        self.assertEqual(self.solution.combinationSum4(nums, target), 0)

    def test_example_3(self):
        nums = [1, 2, 3]
        target = 32
        self.assertEqual(self.solution.combinationSum4(nums, target), 181997601)

    def test_empty_nums(self):
        nums = []
        target = 10
        self.assertEqual(self.solution.combinationSum4(nums, target), 0)


if __name__ == '__main__':
    unittest.main()
