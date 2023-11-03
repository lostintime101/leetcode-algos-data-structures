import unittest
from typing import Optional


"""

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.


Constraints:

The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        leaves = []

        def dfs(node):

            if not node.left and not node.right:
                leaves.append(node.val)

            if node.left: dfs(node.left)
            if node.right: dfs(node.right)

        dfs(root1)
        half = len(leaves)
        dfs(root2)
        return leaves[half:] == leaves[:half]


class TestLeafSimilar(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_leaf_similar_trees(self):
        root1 = TreeNode(3, TreeNode(5), TreeNode(1))
        root2 = TreeNode(3, TreeNode(1), TreeNode(5))
        self.assertTrue(self.solution.leafSimilar(root1, root2))

    def test_non_leaf_similar_trees(self):
        root1 = TreeNode(1, TreeNode(2), TreeNode(3))
        root2 = TreeNode(1, TreeNode(3), TreeNode(2))
        self.assertFalse(self.solution.leafSimilar(root1, root2))

    def test_empty_trees(self):
        self.assertTrue(self.solution.leafSimilar(None, None))


if __name__ == "__main__":
    unittest.main()