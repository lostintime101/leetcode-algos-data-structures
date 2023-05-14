import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root, k: int) -> int:
        values = []

        def dfs(node):
            if not node: return

            values.append(node.val)

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return sorted(values)[k - 1]


class TestKthSmallest(unittest.TestCase):

    def test_single_node_tree(self):
        solution = Solution()
        root = TreeNode(1)
        self.assertEqual(solution.kthSmallest(root, 1), 1)

    def test_two_node_tree(self):
        solution = Solution()
        root = TreeNode(1)
        root.right = TreeNode(2)
        self.assertEqual(solution.kthSmallest(root, 1), 1)
        self.assertEqual(solution.kthSmallest(root, 2), 2)

    def test_three_node_tree(self):
        solution = Solution()
        root = TreeNode(1)
        root.left = TreeNode(0)
        root.right = TreeNode(2)
        self.assertEqual(solution.kthSmallest(root, 1), 0)
        self.assertEqual(solution.kthSmallest(root, 2), 1)
        self.assertEqual(solution.kthSmallest(root, 3), 2)


if __name__ == "__main__":
    unittest.main()
