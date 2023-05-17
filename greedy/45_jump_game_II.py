import unittest

"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].

"""


class Solution:
    def jump(self, nums: [int]) -> int:

        jumps, skip = 0, 0

        for i in range(len(nums) - 1):

            if skip > 0:
                skip -= 1
                continue

            jumps += 1
            l = nums[i]

            if i + l >= len(nums) - 1: return jumps

            jump = nums[i + 1:i + l + 1]
            j = 0

            for k in range(len(jump))[::-1]:
                jump[k] -= j
                j += 1

            skip = jump.index(max(jump))

        return jumps


class TestSolution(unittest.TestCase):

    def test_jump(self):
        nums = [2, 3, 1, 1, 4]
        expected = 2
        solution = Solution()
        self.assertEqual(solution.jump(nums), expected)

        nums = [2, 1, 1, 1, 4]
        expected = 3
        solution = Solution()
        self.assertEqual(solution.jump(nums), expected)

        nums = [1, 2, 3, 4, 5]
        expected = 3
        solution = Solution()
        self.assertEqual(solution.jump(nums), expected)

        nums = [1, 1, 1, 1, 1]
        expected = 4
        solution = Solution()
        self.assertEqual(solution.jump(nums), expected)

        nums = [1, 2, 1, 1, 1]
        expected = 3
        solution = Solution()
        self.assertEqual(solution.jump(nums), expected)

        nums = [5, 1, 1, 1, 1, 1]
        expected = 1
        solution = Solution()
        self.assertEqual(solution.jump(nums), expected)


if __name__ == '__main__':
    unittest.main()
