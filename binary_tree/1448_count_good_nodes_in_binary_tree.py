import unittest

"""

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Constraints:

The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        ret = []

        def dfs(node, max_prev):

            if not node: return

            max_prev = max(node.val, max_prev)

            if node.val >= max_prev: ret.append(1)

            dfs(node.left, max_prev)
            dfs(node.right, max_prev)

        dfs(root, root.val)

        return len(ret)


class TestGoodNodes(unittest.TestCase):

    def test_single_node_tree(self):
        solution = Solution()
        root = TreeNode(1)
        self.assertEqual(solution.goodNodes(root), 1)

    def test_two_node_tree(self):
        solution = Solution()
        root = TreeNode(1)
        root.right = TreeNode(2)
        self.assertEqual(solution.goodNodes(root), 2)

    def test_three_node_tree(self):
        solution = Solution()
        root = TreeNode(1)
        root.left = TreeNode(0)
        root.right = TreeNode(2)
        self.assertEqual(solution.goodNodes(root), 2)

    def test_full_tree(self):
        solution = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        self.assertEqual(solution.goodNodes(root), 7)


if __name__ == "__main__":
    unittest.main()