from typing import Optional
import unittest

"""

A binary tree is named Even-Odd if it meets the following conditions:

The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.

Constraints:

The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 106

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:

        prev, curr = [root], []
        odd = False

        if root.val % 2 != 1: return False

        while prev:
            odd = not odd
            vals = []
            for p in prev:
                vals.append(p.val)
                if p.left: curr.append(p.left)
                if p.right: curr.append(p.right)

            if odd:
                for i in range(len(vals) - 1):
                    if (vals[i] % 2 != 1) or (vals[i] >= vals[i + 1]): return False
                if vals[-1] % 2 != 1: return False
            else:
                for i in range(len(vals) - 1):
                    if (vals[i] % 2) or (vals[i] <= vals[i + 1]): return False
                if vals[-1] % 2: return False

            prev, curr = curr, []

        return True


class TestSolution(unittest.TestCase):
    def test_isEvenOddTree(self):
        # Test Case 1: Valid Even-Odd Tree
        #      1
        #     / \
        #    10  4
        #       / \
        #      3   9
        valid_tree = TreeNode(1, TreeNode(10), TreeNode(4, TreeNode(3), TreeNode(9)))
        self.assertTrue(Solution().isEvenOddTree(valid_tree))

        # Test Case 2: Invalid Even-Odd Tree (even value at level 0)
        #      2
        #     / \
        #    10  4
        #       / \
        #      3   9
        invalid_tree_1 = TreeNode(2, TreeNode(10), TreeNode(4, TreeNode(3), TreeNode(9)))
        self.assertFalse(Solution().isEvenOddTree(invalid_tree_1))

        # Test Case 3: Invalid Even-Odd Tree (not strictly increasing at level 1)
        #      1
        #     / \
        #    10  4
        #       / \
        #      2   9
        invalid_tree_2 = TreeNode(1, TreeNode(10), TreeNode(4, TreeNode(2), TreeNode(9)))
        self.assertFalse(Solution().isEvenOddTree(invalid_tree_2))

        # Test Case 4: Valid Even-Odd Tree (single node)
        #      5
        valid_single_node = TreeNode(5)
        self.assertTrue(Solution().isEvenOddTree(valid_single_node))


if __name__ == '__main__':
    unittest.main()
