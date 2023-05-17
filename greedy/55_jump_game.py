import unittest

"""
You are given an integer array nums. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105

"""

class Solution:
    def canJump(self, nums: [int]) -> bool:

        remain = 1

        for i in range(len(nums) - 1):
            remain -= 1
            if nums[i] > remain: remain = nums[i]
            if remain < 1: return False

        return True


class TestSolution(unittest.TestCase):

    def test_canJump(self):
        nums = [2, 3, 1, 1, 4]
        expected = True
        solution = Solution()
        self.assertEqual(solution.canJump(nums), expected)

        nums = [3, 2, 1, 0, 4]
        expected = False
        solution = Solution()
        self.assertEqual(solution.canJump(nums), expected)

        nums = [1, 1, 1, 1, 1]
        expected = True
        solution = Solution()
        self.assertEqual(solution.canJump(nums), expected)

        nums = [0]
        expected = True
        solution = Solution()
        self.assertEqual(solution.canJump(nums), expected)

        nums = [1, 0, 0, 0, 0]
        expected = False
        solution = Solution()
        self.assertEqual(solution.canJump(nums), expected)

if __name__ == '__main__':
    unittest.main()
