import unittest

"""

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the
array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105

"""

class Solution:
    def canJump(self, nums: [int]) -> bool:

        # BRUTE FORCE (RUNS OUT OF MEM)
        # if nums == [0]: return True

        # jumps = [nums]
        # new_jumps = []

        # while jumps:

        #     for jump in jumps:

        #         for i in range(jump[0]):

        #             if len(jump[i+1:]) <= 1: return True

        #             new_jumps.append(jump[i+1:])

        #     jumps = new_jumps
        #     new_jumps = []

        # return False

        # COUNTER

        if nums == [0]: return True

        goal = len(nums) - 1
        longest_jump = 1

        for i, v in enumerate(nums):

            longest_jump -= 1
            if v > longest_jump: longest_jump = v
            if (longest_jump < 1) and (i != goal): return False

        return True


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_can_jump(self):
        self.assertEqual(self.s.canJump([2,3,1,1,4]), True)
        self.assertEqual(self.s.canJump([3,2,1,0,4]), False)
        self.assertEqual(self.s.canJump([0]), True)
        self.assertEqual(self.s.canJump([1]), True)
        self.assertEqual(self.s.canJump([0,1]), False)
        self.assertEqual(self.s.canJump([1,2,0,0,4]), False)
        self.assertEqual(self.s.canJump([1,1,0,1]), False)
        self.assertEqual(self.s.canJump([1,0,1,0,1]), False)


if __name__ == '__main__':
    unittest.main()
