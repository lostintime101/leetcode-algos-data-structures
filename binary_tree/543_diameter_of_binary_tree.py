import unittest
from typing import Optional

"""

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ret = [0]

        def bfs(node):
            if not node: return 0

            left = bfs(node.left)
            right = bfs(node.right)

            ret[0] = max(ret[0], left + right)
            return max(left, right) + 1

        bfs(root)
        return ret[0]


class DiameterOfBinaryTreeTests(unittest.TestCase):
    def test_diameterOfBinaryTree(self):
        solution = Solution()

        # Test case 1: Empty tree
        root = None
        expected_output = 0
        self.assertEqual(solution.diameterOfBinaryTree(root), expected_output)

        # Test case 2: Tree with a single node
        root = TreeNode(5)
        expected_output = 0
        self.assertEqual(solution.diameterOfBinaryTree(root), expected_output)

        # Test case 3: Tree with multiple nodes
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        expected_output = 3
        self.assertEqual(solution.diameterOfBinaryTree(root), expected_output)

        # Additional test cases...
        # You can add more test cases to further validate the solution

if __name__ == '__main__':
    unittest.main()
