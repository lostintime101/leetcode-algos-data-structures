import unittest
from typing import Optional

"""

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        # edge case, root = []
        if not root: return 0

        min_leaf = [float("inf")]

        def backtrack(node, level):

            if not node: return

            # no need to check lower levels if higher level found
            if level > min_leaf[0]: return

            # is leaf
            if not node.left and not node.right:
                min_leaf[0] = min(min_leaf[0], level)
                return

            if node.left: backtrack(node.left, level + 1)
            if node.right: backtrack(node.right, level + 1)

        backtrack(root, 1)

        return min_leaf[0]


# Unit tests
class TestSolution(unittest.TestCase):

    def test_minDepth(self):
        # Test case 1: Empty tree
        solution = Solution()
        self.assertEqual(solution.minDepth(None), 0)

        # Test case 2: Tree with a single node
        root = TreeNode(1)
        solution = Solution()
        self.assertEqual(solution.minDepth(root), 1)

        # Test case 3: Tree with two levels
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        solution = Solution()
        self.assertEqual(solution.minDepth(root), 2)

        # Test case 4: Tree with three levels
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        solution = Solution()
        self.assertEqual(solution.minDepth(root), 2)

        # Test case 5: Tree with four levels
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        solution = Solution()
        self.assertEqual(solution.minDepth(root), 2)

if __name__ == '__main__':
    unittest.main()
