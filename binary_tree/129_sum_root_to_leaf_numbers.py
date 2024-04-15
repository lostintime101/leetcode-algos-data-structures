import unittest
from typing import Optional

"""
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 9
The depth of the tree will not exceed 10.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, curr):
            curr *= 10
            curr += node.val

            if not node.left and not node.right:
                return curr

            return ((node.left and dfs(node.left, curr)) or 0) + ((node.right and dfs(node.right, curr)) or 0)

        return dfs(root, 0)


class TestSolution(unittest.TestCase):
    def test_sumNumbers(self):
        solution = Solution()

        # Test case 1: Example provided
        #     1
        #    / \
        #   2   3
        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root1.right = TreeNode(3)
        self.assertEqual(solution.sumNumbers(root1), 25)  # (1->2) + (1->3) = 12 + 13 = 25

        # Test case 2: Edge case - single node tree
        root2 = TreeNode(9)
        self.assertEqual(solution.sumNumbers(root2), 9)

        # Test case 3: Tree with only left nodes
        #     4
        #    / \
        #   9   0
        #  / \
        # 5   1
        root3 = TreeNode(4)
        root3.left = TreeNode(9)
        root3.left.left = TreeNode(5)
        root3.left.right = TreeNode(1)
        root3.right = TreeNode(0)
        self.assertEqual(solution.sumNumbers(root3),
                         495 + 491 + 40)  # (4->9->5) + (4->9->1) + (4->0) = 495 + 491 + 40 = 1026

        # Test case 4: Tree with only right nodes
        #     4
        #    / \
        #   0   9
        #      / \
        #     1   5
        root4 = TreeNode(4)
        root4.left = TreeNode(0)
        root4.right = TreeNode(9)
        root4.right.left = TreeNode(1)
        root4.right.right = TreeNode(5)
        self.assertEqual(solution.sumNumbers(root4),
                         40 + 491 + 495)  # (4->0) + (4->9->1) + (4->9->5) = 409 + 491 + 495 = 1395


if __name__ == '__main__':
    unittest.main()
