import unittest

"""
Given an integer array nums of unique elements, return all possible
subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""


class Solution:
    def subsets(self, nums: [int]):

        tree = [[], [nums[0]]]
        if len(nums) == 1: return tree

        nums = nums[1:]

        for num in nums:

            new_leaves = []

            for leaf in tree:
                new_leaf = leaf[:]
                new_leaf.append(num)
                new_leaves.append(new_leaf)

            tree.extend(new_leaves)

        return tree


class TestSubsets(unittest.TestCase):

    def test_empty_list(self):
        s = Solution()
        result = s.subsets([1, 2])
        self.assertEqual(result, [[], [1], [2], [1, 2]])

    def test_one_element_list(self):
        s = Solution()
        result = s.subsets([1])
        self.assertEqual(result, [[], [1]])

    def test_multiple_element_list(self):
        s = Solution()
        result = s.subsets([1, 2, 3])
        self.assertEqual(result, [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])


if __name__ == '__main__':
    unittest.main()
