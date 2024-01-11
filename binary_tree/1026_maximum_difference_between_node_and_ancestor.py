import unittest
from typing import Optional


"""

Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

Constraints:

The number of nodes in the tree is in the range [2, 5000].
0 <= Node.val <= 105


"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        prev, curr = [(root, root.val, root.val)], []
        ans = 0

        while prev:
            for p in prev:
                (node, mi, ma) = p
                if node.val > ma: ma = node.val
                if node.val < mi: mi = node.val
                ans = max(ma-mi, ans)
                if node.left: curr.append((node.left, mi, ma))
                if node.right: curr.append((node.right, mi, ma))

            prev = curr
            curr = []

        return ans


class TestMaxAncestorDiff(unittest.TestCase):

    def test_empty_tree(self):
        self.assertEqual(Solution().maxAncestorDiff(None), 0)

    def test_single_node_tree(self):
        root = TreeNode(8)
        self.assertEqual(Solution().maxAncestorDiff(root), 0)

    def test_balanced_tree(self):
        root = TreeNode(8, TreeNode(3), TreeNode(10))
        self.assertEqual(Solution().maxAncestorDiff(root), 7)

    def test_unbalanced_tree(self):
        root = TreeNode(1, TreeNode(2), TreeNode(0, TreeNode(3), TreeNode(4)))
        self.assertEqual(Solution().maxAncestorDiff(root), 4)

    def test_large_tree(self):
        root = TreeNode(543, TreeNode(225), TreeNode(924, TreeNode(401), TreeNode(954)))
        self.assertEqual(Solution().maxAncestorDiff(root), 729)

    def test_all_same_value_tree(self):
        root = TreeNode(5, TreeNode(5), TreeNode(5))
        self.assertEqual(Solution().maxAncestorDiff(root), 0)
