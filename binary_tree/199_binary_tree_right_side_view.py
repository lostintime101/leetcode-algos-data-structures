import unittest
import collections

"""

Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: [TreeNode]) -> [int]:

        # BFS WITHOUT DEQUE
        # if not root: return []

        # values, curr_values = [root.val], []
        # prev, curr = [root], []

        # while prev:

        #     for node in prev:

        #         if node.left:
        #             curr.append(node.left)
        #             curr_values.append(node.left.val)
        #         if node.right:
        #             curr.append(node.right)
        #             curr_values.append(node.right.val)

        #     prev = curr
        #     curr = []
        #     if prev: values.append(curr_values[-1])

        # return values

        # BFS WITH DEQUE

        if not root: return []
        ret = []
        q = collections.deque([root])

        while q:

            for i in range(len(q)):
                node = q.popleft()
                if node:
                    rightside = node
                    q.append(node.left)
                    q.append(node.right)

            if q: ret.append(rightside.val)

        return ret


class TestRightSideView(unittest.TestCase):
    def test_empty_tree(self):
        solution = Solution()
        self.assertEqual(solution.rightSideView(None), [])

    def test_single_node_tree(self):
        solution = Solution()
        root = TreeNode(1)
        self.assertEqual(solution.rightSideView(root), [1])

    def test_two_node_tree(self):
        solution = Solution()
        root = TreeNode(1)
        root.right = TreeNode(2)
        self.assertEqual(solution.rightSideView(root), [1, 2])

    def test_three_node_tree(self):
        solution = Solution()
        root = TreeNode(1)
        root.left = TreeNode(0)
        root.right = TreeNode(2)
        self.assertEqual(solution.rightSideView(root), [1, 2])

    def test_full_tree(self):
        solution = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        self.assertEqual(solution.rightSideView(root), [1, 3, 7])


if __name__ == "__main__":
    unittest.main()