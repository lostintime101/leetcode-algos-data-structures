import unittest
from typing import Optional

"""
Given a binary tree, determine if it is height-balanced.

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        ret = [1]

        def dfs(node):

            if not node: return 1

            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) > 1: ret[0] = 0

            return max(left, right) + 1

        dfs(root)
        return ret[0]



class IsBalancedTests(unittest.TestCase):
    def test_isBalanced(self):
        solution = Solution()

        # Test case 1: Empty tree
        root = None
        expected_output = True
        self.assertEqual(solution.isBalanced(root), expected_output)

        # Test case 2: Tree with a single node
        root = TreeNode(5)
        expected_output = True
        self.assertEqual(solution.isBalanced(root), expected_output)

        # Test case 3: Balanced tree with multiple nodes
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        expected_output = True
        self.assertEqual(solution.isBalanced(root), expected_output)

        # Test case 4: Unbalanced tree with multiple nodes
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        expected_output = False
        self.assertEqual(solution.isBalanced(root), expected_output)

        # Additional test cases...
        # You can add more test cases to further validate the solution

if __name__ == '__main__':
    unittest.main()
