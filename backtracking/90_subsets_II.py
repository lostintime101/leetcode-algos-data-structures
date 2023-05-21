import unittest

"""

Given an integer array nums that may contain duplicates, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10

"""

class Solution:
    def subsetsWithDup(self, nums: [int]) -> [[int]]:

        # BACKTRACK
        ret, i = [], -1
        nums = sorted(nums)

        def backtrack(i, prev):

            i += 1

            if i > len(nums) - 1:
                if prev not in ret:
                    ret.append(prev.copy())
                return

            prev.append(nums[i])
            backtrack(i, prev)
            prev.pop()
            backtrack(i, prev)

        backtrack(i, [])

        return ret



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_subsetsWithDup(self):
        nums = [1, 2, 2]
        expected = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
        result = self.solution.subsetsWithDup(nums)
        self.assertEqual(sorted(result), sorted(expected))

        nums = [0]
        expected = [[], [0]]
        result = self.solution.subsetsWithDup(nums)
        self.assertEqual(sorted(result), sorted(expected))

        nums = [1, 2, 3]
        expected = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
        result = self.solution.subsetsWithDup(nums)
        self.assertEqual(sorted(result), sorted(expected))

if __name__ == '__main__':
    unittest.main()
