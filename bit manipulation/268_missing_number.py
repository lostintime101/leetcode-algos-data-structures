import unittest
from typing import List

"""

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Constraints:

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.

"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        return (sum([num for num in range(1, len(nums)+1)]) - sum(nums))

        # n = [i for i in range(0, len(nums))]
        # return [num for num in nums if num not in n]


class SolutionTests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_missingNumber_example1(self):
        result = self.solution.missingNumber([3, 0, 1])
        self.assertEqual(result, 2)

    def test_missingNumber_example2(self):
        result = self.solution.missingNumber([0, 1])
        self.assertEqual(result, 2)

    def test_missingNumber_example3(self):
        result = self.solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])
        self.assertEqual(result, 8)

    def test_missingNumber_singleElement(self):
        result = self.solution.missingNumber([0])
        self.assertEqual(result, 1)

    def test_missingNumber_largeInput(self):
        result = self.solution.missingNumber([i for i in range(1000001)])
        self.assertEqual(result, 1000001)

if __name__ == '__main__':
    unittest.main()
