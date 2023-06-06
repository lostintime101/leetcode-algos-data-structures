import unittest
from typing import Optional

""""

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q: return True

        if (q and not p) or (p and not q) or (p.val != q.val): return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class IsSameTreeTests(unittest.TestCase):
    def test_isSameTree(self):
        solution = Solution()

        # Test case 1: Empty trees
        p = None
        q = None
        expected_output = True
        self.assertEqual(solution.isSameTree(p, q), expected_output)

        # Test case 2: Single node trees, same node values
        p = TreeNode(5)
        q = TreeNode(5)
        expected_output = True
        self.assertEqual(solution.isSameTree(p, q), expected_output)

        # Test case 3: Single node trees, different node values
        p = TreeNode(5)
        q = TreeNode(10)
        expected_output = False
        self.assertEqual(solution.isSameTree(p, q), expected_output)

        # Test case 4: Trees with multiple nodes, same structure and node values
        p = TreeNode(3)
        p.left = TreeNode(4)
        p.right = TreeNode(5)
        q = TreeNode(3)
        q.left = TreeNode(4)
        q.right = TreeNode(5)
        expected_output = True
        self.assertEqual(solution.isSameTree(p, q), expected_output)

        # Test case 5: Trees with multiple nodes, different structure
        p = TreeNode(3)
        p.left = TreeNode(4)
        p.right = TreeNode(5)
        q = TreeNode(3)
        q.left = TreeNode(5)  # Different structure compared to the corresponding node in the other tree
        q.right = TreeNode(4)
        expected_output = False
        self.assertEqual(solution.isSameTree(p, q), expected_output)

        # Additional test cases...
        # You can add more test cases to further validate the solution

if __name__ == '__main__':
    unittest.main()


