import unittest
from typing import Optional
import heapq
"""

Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

Constraints:

The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        # HEAP
        values = []

        def dfs(node):
            if not node: return
            heapq.heappush(values, node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        ret = float("inf")
        prev = heapq.heappop(values)
        while values:
            curr = heapq.heappop(values)
            ret = min(ret, curr - prev)
            prev = curr

        return ret

class TestSolution(unittest.TestCase):

    def test_getMinimumDifference(self):
        # Test case 1: Balanced tree with minimum difference 1
        root1 = TreeNode(4)
        root1.left = TreeNode(2)
        root1.right = TreeNode(6)
        root1.left.left = TreeNode(1)
        root1.left.right = TreeNode(3)
        self.assertEqual(Solution().getMinimumDifference(root1), 1)

        # Test case 2: Tree with minimum difference 2, right-skewed
        root2 = TreeNode(1)
        root2.right = TreeNode(3)
        root2.right.right = TreeNode(5)
        root2.right.right.right = TreeNode(7)
        self.assertEqual(Solution().getMinimumDifference(root2), 2)

if __name__ == '__main__':
    unittest.main()
