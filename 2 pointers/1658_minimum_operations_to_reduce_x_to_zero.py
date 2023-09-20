import unittest
from typing import List
from collections import deque


"""


You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
1 <= x <= 109


"""


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        ans = float('inf')
        nums = deque(nums)
        old_left, old_right = [], []

        curr = 0

        while nums and curr <= x:

            left = nums.popleft()
            curr += left
            old_left.append(left)

            if curr == x:
                ans = min(ans, len(old_left, ) + len(old_right))
                break

        while nums and old_left:
            top_left = old_left.pop()
            curr -= top_left
            nums.appendleft(top_left)

            if curr == x: ans = min(ans, len(old_left, ) + len(old_right))

            while nums and curr < x:
                right = nums.pop()
                curr += right
                old_right.append(right)

                if curr == x: ans = min(ans, len(old_left, ) + len(old_right))

        if ans == float('inf'): return -1
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 1, 4, 2, 3]
        x = 5
        result = self.solution.minOperations(nums, x)
        self.assertEqual(result, 2)

    def test_example_2(self):
        nums = [5, 6, 7, 8, 9]
        x = 4
        result = self.solution.minOperations(nums, x)
        self.assertEqual(result, -1)

    def test_example_3(self):
        nums = [3, 2, 20, 1, 1, 3]
        x = 10
        result = self.solution.minOperations(nums, x)
        self.assertEqual(result, 5)

    def test_example_4(self):
        nums = [1, 1]
        x = 3
        result = self.solution.minOperations(nums, x)
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()
