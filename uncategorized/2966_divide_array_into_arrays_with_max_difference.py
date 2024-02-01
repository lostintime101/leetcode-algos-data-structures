from typing import List
import unittest

"""

You are given an integer array nums of size n and a positive integer k.

Divide the array into one or more arrays of size 3 satisfying the following conditions:

Each element of nums should be in exactly one array.
The difference between any two elements in one array is less than or equal to k.
Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.


Constraints:

n == nums.length
1 <= n <= 105
n is a multiple of 3.
1 <= nums[i] <= 105
1 <= k <= 105

"""

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:

        if len(nums) % 3: return []
        nums = sorted(nums)
        ans, curr = [], []

        for i, v in enumerate(nums):

            curr.append(v)

            if i % 3 == 2:
                if (curr[2] - curr[0]) > k: return []
                ans.append(curr)
                curr = []

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_divide_array_valid_input(self):
        nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        k = 5
        expected_result = []

        result = self.solution.divideArray(nums, k)

        self.assertEqual(result, expected_result)

    def test_divide_array_invalid_input(self):
        nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]  # Not divisible by 3
        k = 5

        result = self.solution.divideArray(nums, k)

        self.assertEqual(result, [])

    def test_divide_array_large_difference(self):
        nums = [1, 2, 8, 4, 5, 9, 2, 6, 5, 3, 5]
        k = 5

        result = self.solution.divideArray(nums, k)

        self.assertEqual(result, [])

    def test_divide_array_empty_input(self):
        nums = []
        k = 5

        result = self.solution.divideArray(nums, k)

        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
