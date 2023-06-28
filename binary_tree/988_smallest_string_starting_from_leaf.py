import unittest
from typing import Optional

""""

You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

For example, "ab" is lexicographically smaller than "aba".
A leaf of a node is a node that has no children.

Constraints:

The number of nodes in the tree is in the range [1, 8500].
0 <= Node.val <= 25
 

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:

        shortest_word = [[26]]

        def backtrack(node, word):
            word.append(node.val)

            if (not node.left) and (not node.right):
                shortest_word[0] = min(shortest_word[0], word[::-1])
                word.pop()
                return

            if node.left: backtrack(node.left, word)
            if node.right: backtrack(node.right, word)
            word.pop()

        backtrack(root, [])

        word = ""
        for i in range(len(shortest_word[0])):
            shortest_word[0][i] = chr(shortest_word[0][i] + 97)

        return "".join(shortest_word[0])



class TestSolution(unittest.TestCase):
    def test_smallestFromLeaf(self):
        # Test case 1
        #   a
        #  / \
        # b   c
        #    / \
        #   d   e
        root1 = TreeNode(ord('a') - 97)
        root1.left = TreeNode(ord('b') - 97)
        root1.right = TreeNode(ord('c') - 97)
        root1.right.left = TreeNode(ord('d') - 97)
        root1.right.right = TreeNode(ord('e') - 97)
        solution = Solution()
        self.assertEqual(solution.smallestFromLeaf(root1), "ba")

        # Test case 2
        #   z
        #  / \
        # y   x
        #    / \
        #   w   v
        root2 = TreeNode(ord('z') - 97)
        root2.left = TreeNode(ord('y') - 97)
        root2.right = TreeNode(ord('x') - 97)
        root2.right.left = TreeNode(ord('w') - 97)
        root2.right.right = TreeNode(ord('v') - 97)
        solution = Solution()
        self.assertEqual(solution.smallestFromLeaf(root2), "vxz")

        # Test case 3
        #   c
        #  / \
        # b   a
        #    / \
        #   d   e
        root3 = TreeNode(ord('c') - 97)
        root3.left = TreeNode(ord('b') - 97)
        root3.right = TreeNode(ord('a') - 97)
        root3.right.left = TreeNode(ord('d') - 97)
        root3.right.right = TreeNode(ord('e') - 97)
        solution = Solution()
        self.assertEqual(solution.smallestFromLeaf(root3), "bc")


if __name__ == '__main__':
    unittest.main()
