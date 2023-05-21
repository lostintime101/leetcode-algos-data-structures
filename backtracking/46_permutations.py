import unittest

"""

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.

"""

class Solution:
    def permute(self, nums: [int]) -> [[int]]:

        # BACKTRACK
        ret = []

        def backtrack(curr, remains):

            if len(curr) == len(nums):
                ret.append(curr[::])
                return

            remains2 = remains[::]

            for i in range(len(remains)):
                curr.append(remains[i])
                remains2.remove(remains[i])
                backtrack(curr, remains2)
                remains2 = remains[::]
                curr.pop()

        backtrack([], nums)

        return ret

        #  PYTHON IN BUILT FUNCTION
        # return permutations(nums)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_permute(self):
        nums = [1, 2, 3]
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        result = self.solution.permute(nums)
        self.assertEqual(sorted(result), sorted(expected))

        nums = [0, 1]
        expected = [[0, 1], [1, 0]]
        result = self.solution.permute(nums)
        self.assertEqual(sorted(result), sorted(expected))

        nums = [1]
        expected = [[1]]
        result = self.solution.permute(nums)
        self.assertEqual(sorted(result), sorted(expected))

if __name__ == '__main__':
    unittest.main()
