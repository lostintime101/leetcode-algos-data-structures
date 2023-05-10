import unittest
from collections import deque

"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root) -> int:

        # RECURSION
        # if not root : return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # BFS WITH QUEUE
        level = 0
        q = deque([root])

        while q:

            level += 1
            for i in range(len(q)):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

        return level

        # DFS
        # # deal with edge case of zero nodes
        # max_depth = 0
        # if  root == None:
        #     return max_depth

        # # 2 lists to collect nodes
        # current_nodes = [root]
        # next_nodes = []

        # while current_nodes:

        #     # add next layer's nodes to next_nodes
        #     for node in current_nodes:
        #         if node.left:
        #             next_nodes.append(node.left)
        #         if node.right:
        #             next_nodes.append(node.right)

        #     # next nodes becomes current nodes
        #     current_nodes = next_nodes

        #     # 1 layer deeper, reset next_nodes
        #     next_nodes = []
        #     max_depth += 1

        # return max_depth


class MaxDepthTestCase(unittest.TestCase):
    def test_maxDepth_recursion(self):
        # Create a binary tree with a depth of 3
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        solution = Solution()
        self.assertEqual(solution.maxDepth(root), 3)

    def test_maxDepth_bfs(self):
        # Create a binary tree with a depth of 4
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        root.right.right.left = TreeNode(10)

        solution = Solution()
        self.assertEqual(solution.maxDepth(root), 4)

    def test_maxDepth_dfs(self):
        # Create a binary tree with a depth of 2
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)

        solution = Solution()
        self.assertEqual(solution.maxDepth(root), 3)

# Run the tests
unittest.main()