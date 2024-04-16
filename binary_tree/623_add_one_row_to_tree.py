import sys
import unittest
from typing import Optional

"""

Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.

Note that the root node is at depth 1.

The adding rule is:

Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
cur's original left subtree should be the left subtree of the new left subtree root.
cur's original right subtree should be the right subtree of the new right subtree root.
If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.

Constraints:

The number of nodes in the tree is in the range [1, 104].
The depth of the tree is in the range [1, 104].
-100 <= Node.val <= 100
-105 <= val <= 105
1 <= depth <= the depth of tree + 1

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        prev = [root]
        curr = []
        curr_level = 1

        if depth == 1:
            return TreeNode(val=val, left=root, right=None)

        while prev:

            if curr_level > depth: return root

            if curr_level == depth - 1:

                for p in prev:

                    nw_left = TreeNode(val=val, left=None, right=None)
                    nw_right = TreeNode(val=val, left=None, right=None)

                    if p.left: nw_left.left = p.left

                    if p.right: nw_right.right = p.right

                    p.left = nw_left
                    curr.append(nw_left)
                    p.right = nw_right
                    curr.append(nw_right)

            else:
                for p in prev:
                    if p.left:
                        curr.append(p.left)
                    if p.right:
                        curr.append(p.right)

            curr_level += 1
            prev = curr
            curr = []

        return root


class TestSolution(unittest.TestCase):
    def test_addOneRow(self):
        # Test case 1: Adding a row at depth 1 to a tree with one node
        root1 = TreeNode(val=4)
        solution = Solution()
        new_root1 = solution.addOneRow(root1, 2, 1)
        self.assertEqual(new_root1.val, 2)
        self.assertEqual(new_root1.left.val, 4)
        self.assertIsNone(new_root1.right)

        # Test case 2: Adding a row at depth 2 to a tree with one node
        root2 = TreeNode(val=4)
        new_root2 = solution.addOneRow(root2, 2, 2)
        self.assertEqual(new_root2.val, 4)
        self.assertEqual(new_root2.left.val, 2)
        self.assertEqual(new_root2.right.val, 2)

        # Test case 3: Adding a row at depth 2 to a tree with multiple nodes
        root3 = TreeNode(val=4, left=TreeNode(val=2), right=TreeNode(val=6))
        new_root3 = solution.addOneRow(root3, 3, 2)
        self.assertEqual(new_root3.val, 4)
        self.assertEqual(new_root3.left.val, 3)
        self.assertEqual(new_root3.left.left.val, 2)
        self.assertEqual(new_root3.right.val, 3)
        self.assertEqual(new_root3.right.right.val, 6)


if __name__ == '__main__':
    unittest.main()
