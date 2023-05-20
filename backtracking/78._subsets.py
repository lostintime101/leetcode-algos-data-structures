"""

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.

"""

class Solution:
    def subsets(self, nums: [int]) -> [[int]]:
        # tree = [[], [nums[0]]]
        # if len(nums) == 1: return tree

        # nums = nums[1:]

        # for num in nums:

        #     new_leaves = []

        #     for leaf in tree:
        #         new_leaf = leaf[:]
        #         new_leaf.append(num)
        #         new_leaves.append(new_leaf)

        #     tree.extend(new_leaves)

        # return tree

        # BACKTRACKING

        ret = []

        def dfs(i, curr):
            if i > len(nums) - 1:
                ret.append(curr.copy())
                return

            curr.append(nums[i])
            dfs(i + 1, curr)
            curr.pop()
            dfs(i + 1, curr)

        dfs(0, [])

        return ret

def run_tests():
    solution = Solution()

    # Test case 1
    nums = [1, 2, 3]
    # The expected output is [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    assert set(map(tuple, solution.subsets(nums))) == set(map(tuple, [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]))

    # Test case 2
    nums = [4, 5, 6]
    # The expected output is [[], [4], [5], [6], [4, 5], [4, 6], [5, 6], [4, 5, 6]]
    assert set(map(tuple, solution.subsets(nums))) == set(map(tuple, [[], [4], [5], [6], [4, 5], [4, 6], [5, 6], [4, 5, 6]]))

    # Test case 3
    nums = [7, 8]
    # The expected output is [[], [7], [8], [7, 8]]
    assert set(map(tuple, solution.subsets(nums))) == set(map(tuple, [[], [7], [8], [7, 8]]))

    # Test case 4: Empty input
    nums = []
    # The expected output is [[]]
    assert set(map(tuple, solution.subsets(nums))) == set(map(tuple, [[]]))

    # Test case 5: Single element
    nums = [9]
    # The expected output is [[], [9]]
    assert set(map(tuple, solution.subsets(nums))) == set(map(tuple, [[], [9]]))

    print("All tests passed!")


run_tests()
