import unittest
from typing import Optional

"""

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 30,000 nodes
        ret = [float("-inf")]

        def dfs(node):
            if not node: return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            ret[0] = max(right + left + node.val, ret[0])

            return node.val + max(left, right, 0)

        dfs(root)

        return ret[0]


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Implementation of maxPathSum method

        # Unit tests for the Solution class
        class SolutionTestCase(unittest.TestCase):
            def test_maxPathSum(self):
                # Create a sample binary tree
                root = TreeNode(1)
                root.left = TreeNode(2)
                root.right = TreeNode(3)

                # Create solution object
                solution = Solution()

                # Calculate the maximum path sum
                max_sum = solution.maxPathSum(root)

                # Verify the maximum path sum
                self.assertEqual(max_sum, 6)

            def test_maxPathSum_with_negative_values(self):
                # Create a sample binary tree with negative values
                root = TreeNode(-10)
                root.left = TreeNode(9)
                root.right = TreeNode(20)
                root.right.left = TreeNode(15)
                root.right.right = TreeNode(7)

                # Create solution object
                solution = Solution()

                # Calculate the maximum path sum
                max_sum = solution.maxPathSum(root)

                # Verify the maximum path sum
                self.assertEqual(max_sum, 42)

            def test_maxPathSum_empty_tree(self):
                # Create an empty binary tree
                root = None

                # Create solution object
                solution = Solution()

                # Calculate the maximum path sum
                max_sum = solution.maxPathSum(root)

                # Verify that the maximum path sum is 0 for an empty tree
                self.assertEqual(max_sum, 0)


if __name__ == '__main__':
    unittest.main()
