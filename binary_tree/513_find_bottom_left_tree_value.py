import unittest
from typing import Optional

"""
Given the root of a binary tree, return the leftmost value in the last row of the tree.

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        prev = [root]
        curr = []
        ans = None
        while prev:
            ans = prev[0].val
            for p in prev:
                if p.left:
                    curr.append(p.left)
                if p.right:
                    curr.append(p.right)

            prev = curr
            curr = []

        return ans


class TestFindBottomLeftValue(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        # Create a simple binary tree
        #     1
        #    / \
        #   2   3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(self.solution.findBottomLeftValue(root), 2)

    def test_case2(self):
        # Create a binary tree with multiple levels
        #       1
        #      / \
        #     2   3
        #    / \   \
        #   4   5   6
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(6)
        self.assertEqual(self.solution.findBottomLeftValue(root), 4)

    def test_case3(self):
        # Test with a single node tree
        #   1
        root = TreeNode(1)
        self.assertEqual(self.solution.findBottomLeftValue(root), 1)


if __name__ == '__main__':
    unittest.main()
