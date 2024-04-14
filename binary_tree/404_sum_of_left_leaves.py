import unittest
from typing import Optional

"""

Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def dfs(node, left):

            if not node:
                return 0

            if not node.left and not node.right and left:
                return node.val

            return dfs(node.left, True) + dfs(node.right, False)

        return dfs(root.left, True) + dfs(root.right, False)


import unittest


# Define the TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Define the Solution class
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def dfs(node, left):

            if not node:
                return 0

            if not node.left and not node.right and left:
                return node.val

            return dfs(node.left, True) + dfs(node.right, False)

        return dfs(root, False)


class TestSolution(unittest.TestCase):

    def test_sumOfLeftLeaves(self):
        # Test case 1
        #   3
        #  / \
        # 9  20
        #   /  \
        #  15   7
        root1 = TreeNode(3)
        root1.left = TreeNode(9)
        root1.right = TreeNode(20)
        root1.right.left = TreeNode(15)
        root1.right.right = TreeNode(7)
        self.assertEqual(Solution().sumOfLeftLeaves(root1), 24)

        # Test case 2
        #     1
        #    / \
        #   2   3
        #  / \
        # 4   5
        root2 = TreeNode(1)
        root2.left = TreeNode(2)
        root2.right = TreeNode(3)
        root2.left.left = TreeNode(4)
        root2.left.right = TreeNode(5)
        self.assertEqual(Solution().sumOfLeftLeaves(root2), 4)

        # Test case 3
        #     1
        #    / \
        #   2   3
        #  / \  /
        # 4   5 6
        root3 = TreeNode(1)
        root3.left = TreeNode(2)
        root3.right = TreeNode(3)
        root3.left.left = TreeNode(4)
        root3.left.right = TreeNode(5)
        root3.right.left = TreeNode(6)
        self.assertEqual(Solution().sumOfLeftLeaves(root3), 10)


if __name__ == '__main__':
    unittest.main()
