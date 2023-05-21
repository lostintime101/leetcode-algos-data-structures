import unittest

"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations 
of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40

"""

class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:

        # BACKTRACKISH SOLUTION
        set_of_lists = set()

        def backtrack(curr):

            if sum(curr) > target: return

            if sum(curr) == target:
                curr = sorted(curr)
                set_of_lists.add(tuple(curr))

                return

            for num in candidates:
                curr2 = curr[::]
                curr2.append(num)
                backtrack(curr2)

        backtrack([])

        return [list(item) for item in set_of_lists]



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_combinationSum(self):
        candidates = [2, 3, 6, 7]
        target = 7
        expected = [[2, 2, 3], [7]]
        result = self.solution.combinationSum(candidates, target)
        self.assertEqual(sorted(result), sorted(expected))

        candidates = [2, 3, 5]
        target = 8
        expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        result = self.solution.combinationSum(candidates, target)
        self.assertEqual(sorted(result), sorted(expected))

        candidates = [2, 3]
        target = 1
        expected = []
        result = self.solution.combinationSum(candidates, target)
        self.assertEqual(sorted(result), sorted(expected))

        candidates = [1]
        target = 1
        expected = [[1]]
        result = self.solution.combinationSum(candidates, target)
        self.assertEqual(sorted(result), sorted(expected))

if __name__ == '__main__':
    unittest.main()
