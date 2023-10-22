from typing import List
import unittest

"""

You are given an array of integers nums (0-indexed) and an integer k.

The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j.

Return the maximum possible score of a good subarray.

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 2 * 104
0 <= k < nums.length

"""

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:

        mins = [0] * len(nums)

        mini = nums[k]
        for i in range(k, len(nums)):
            mini = min(mini, nums[i])
            mins[i] = mini

        mini = nums[k]
        for i in range(k, -1, -1):
            mini = min(mini, nums[i])
            mins[i] = mini

        ret = nums[k]

        l, r = k, k

        while not (l == 0 and r == len(nums) - 1):

            curr = min(mins[l], mins[r]) * (r - l + 1)

            ret = max(curr, ret)

            if l == 0:
                r += 1
                continue
            if r == len(nums) - 1:
                l -= 1
                continue

            if mins[l - 1] < mins[r + 1]:
                r += 1
            else:
                l -= 1

        curr = min(mins[l], mins[r]) * (r - l + 1)
        ret = max(curr, ret)

        return ret


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case_1(self):
        nums = [1, 4, 3, 7, 4, 5]
        k = 3
        self.assertEqual(self.solution.maximumScore(nums, k), 15)

    def test_example_case_2(self):
        nums = [5, 5, 4, 5, 4, 1, 1, 1]
        k = 0
        self.assertEqual(self.solution.maximumScore(nums, k), 20)

    def test_edge_case_single_element(self):
        nums = [5]
        k = 0
        self.assertEqual(self.solution.maximumScore(nums, k), 5)

    def test_edge_case_all_equal_elements(self):
        nums = [1, 1, 1, 1, 1]
        k = 2
        self.assertEqual(self.solution.maximumScore(nums, k), 5)


if __name__ == "__main__":
    unittest.main()


