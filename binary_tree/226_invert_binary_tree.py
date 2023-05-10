import unittest
from typing import Optional

"""
Given the root of a binary tree, invert the tree, and return its root.

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # Recusion
        if not root: return root

        def swap(node):

            if not node: return

            node.left, node.right = node.right, node.left

            swap(node.left)
            swap(node.right)

        swap(root)

        return root


# Define the unit tests
class InvertTreeTestCase(unittest.TestCase):
    def test_invertTree(self):
        # Create a binary tree
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)

        # Expected inverted tree
        expected_root = TreeNode(4)
        expected_root.left = TreeNode(7)
        expected_root.right = TreeNode(2)
        expected_root.left.left = TreeNode(9)
        expected_root.left.right = TreeNode(6)
        expected_root.right.left = TreeNode(3)
        expected_root.right.right = TreeNode(1)

        solution = Solution()
        inverted_tree = solution.invertTree(root)

        # Check if the inverted tree is equal to the expected inverted tree
        self.assertTrue(self.isSameTree(inverted_tree, expected_root))

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Helper method to check if two trees are the same
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


unittest.main()