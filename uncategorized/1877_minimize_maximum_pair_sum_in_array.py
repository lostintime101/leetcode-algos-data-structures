import unittest
from typing import List

"""

The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.

For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.
Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:

Each element of nums is in exactly one pair, and
The maximum pair sum is minimized.
Return the minimized maximum pair sum after optimally pairing up the elements.


Constraints:

n == nums.length
2 <= n <= 105
n is even.
1 <= nums[i] <= 105


"""

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        ans = 0

        for i in range(len(nums) // 2):
            ans = max(ans, nums[i] + nums[len(nums) - (i + 1)])

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minPairSum_basic(self):
        nums = [3, 5, 2, 4, 1]
        result = self.solution.minPairSum(nums)
        self.assertEqual(result, 6)

    def test_minPairSum_emptyList(self):
        nums = []
        result = self.solution.minPairSum(nums)
        self.assertEqual(result, 0)

    def test_minPairSum_singleElement(self):
        nums = [7]
        result = self.solution.minPairSum(nums)
        self.assertEqual(result, 0)

    def test_minPairSum_oddLength(self):
        nums = [3, 5, 2, 4, 1, 6]
        result = self.solution.minPairSum(nums)
        self.assertEqual(result, 7)

    def test_minPairSum_negativeNumbers(self):
        nums = [-3, 5, -2, 4, 1]
        result = self.solution.minPairSum(nums)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
