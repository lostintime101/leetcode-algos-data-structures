import unittest
from typing import Optional

"""

Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Constraints:

The number of nodes in the tree is in the range [1, 25].
1 <= Node.val <= 231 - 1
root.val == min(root.left.val, root.right.val) for each internal node of the tree.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:

        ret = set()

        def dfs(node):
            if not node: return

            ret.add(node.val)

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        a = min(ret)
        ret.remove(a)
        if ret: b = min(ret)

        if not ret: return -1
        return b



class TestSolution(unittest.TestCase):

    def test_findSecondMinimumValue(self):
        solution = Solution()

        # Test case 1
        root = TreeNode(2)
        root.left = TreeNode(2)
        root.right = TreeNode(5)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(7)
        expected = 5
        self.assertEqual(solution.findSecondMinimumValue(root), expected)

        # Test case 2
        root = TreeNode(2)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        expected = -1  # No second minimum value
        self.assertEqual(solution.findSecondMinimumValue(root), expected)

        # Test case 3
        root = TreeNode(2)
        expected = -1  # Only one node, so no second minimum value
        self.assertEqual(solution.findSecondMinimumValue(root), expected)

        # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
