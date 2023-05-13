import unittest

"""

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q
as descendants (where we allow a node to be a descendant of itself).”

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root


class LowestCommonAncestorTests(unittest.TestCase):

    def test_lowestCommonAncestor_case1(self):
        # Test Case 1
        #   6
        #  / \
        # 2   8
        #    / \
        #   0   4
        #      / \
        #     3   5
        # p = 2, q = 8
        # The lowest common ancestor is 6.
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(4)
        root.right.right.left = TreeNode(3)
        root.right.right.right = TreeNode(5)
        p = root.left
        q = root.right
        result = Solution().lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 6)

    def test_lowestCommonAncestor_case2(self):
        # Test Case 2
        #   6
        #  / \
        # 2   8
        #    / \
        #   0   4
        #      / \
        #     3   5
        # p = 2, q = 4
        # The lowest common ancestor is 6.
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(4)
        root.right.right.left = TreeNode(3)
        root.right.right.right = TreeNode(5)
        p = root.left
        q = root.right.right
        result = Solution().lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 6)

    def test_lowestCommonAncestor_case3(self):
        # Test Case 3
        #   6
        #  / \
        # 2   8
        #    / \
        #   0   4
        #      / \
        #     3   5
        # p = 3, q = 5
        # The lowest common ancestor is 4.
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(4)
        root.right.right.left = TreeNode(3)
        root.right.right.right = TreeNode(5)
        p = root.right.right.left
        q = root.right.right.right
        result = Solution().lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 4)

if __name__ == '__main__':
    unittest.main()