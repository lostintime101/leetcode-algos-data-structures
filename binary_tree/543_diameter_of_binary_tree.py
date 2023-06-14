import unittest
from typing import Optional

"""

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.maximum = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node: return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.maximum = max(self.maximum, left + right)

            return 1 + max(left, right)

        dfs(root)

        return self.maximum



class TestSolution(unittest.TestCase):

    def test_diameterOfBinaryTree(self):
        # Test case 1: Balanced tree with diameter 3
        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root1.right = TreeNode(3)
        root1.left.left = TreeNode(4)
        root1.left.right = TreeNode(5)
        self.assertEqual(Solution().diameterOfBinaryTree(root1), 3)

        # Test case 2: Tree with diameter 4, right-skewed
        root2 = TreeNode(1)
        root2.right = TreeNode(2)
        root2.right.right = TreeNode(3)
        root2.right.right.right = TreeNode(4)
        self.assertEqual(Solution().diameterOfBinaryTree(root2), 3)

        # Test case 3: Tree with diameter 0, single node
        root3 = TreeNode(1)
        self.assertEqual(Solution().diameterOfBinaryTree(root3), 0)

        # Test case 4: Empty tree
        self.assertEqual(Solution().diameterOfBinaryTree(None), 0)

if __name__ == '__main__':
    unittest.main()
