import unittest
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        triggerVal = subRoot.val
        ret = [0]

        def areSame(root1, root2):

            if not root1 and not root2: return True
            if (root1 and not root2) or (root2 and not root1) or (root1.val != root2.val): return False

            return areSame(root1.left, root2.left) and areSame(root1.right, root2.right)

        def dfs(node):

            if not node: return
            if node.val == triggerVal:
                if areSame(node, subRoot): ret[0] = 1

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ret[0]



# implementation of isSubtree method

class IsSubtreeTests(unittest.TestCase):
    def test_isSubtree(self):
        solution = Solution()

        # Test case 1: Empty trees
        root = None
        subRoot = None
        expected_output = True
        self.assertEqual(solution.isSubtree(root, subRoot), expected_output)

        # Test case 2: Single node trees, same node values
        root = TreeNode(5)
        subRoot = TreeNode(5)
        expected_output = True
        self.assertEqual(solution.isSubtree(root, subRoot), expected_output)

        # Test case 3: Single node trees, different node values

