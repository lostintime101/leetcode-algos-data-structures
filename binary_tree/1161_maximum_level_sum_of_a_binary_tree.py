import unittest
from typing import Optional

"""

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        ret = [float("-inf"), 0]
        prev, curr, level = [root], [], 1

        while prev:

            levelsum = 0

            for node in prev:
                levelsum += node.val
                if node.left: curr.append(node.left)
                if node.right: curr.append(node.right)

            if levelsum > ret[0]:
                ret[0] = levelsum
                ret[1] = level

            prev, curr = curr, []
            level += 1

        return ret[1]



class SolutionTests(unittest.TestCase):
    def test_maxLevelSum(self):
        solution = Solution()

        # Test case 1: Maximum level sum is 15 (level 3)
        #    1
        #   / \
        #  7   0
        # / \
        # 7  8
        root = TreeNode(1)
        root.left = TreeNode(7)
        root.right = TreeNode(0)
        root.left.left = TreeNode(7)
        root.left.right = TreeNode(8)

        self.assertEqual(solution.maxLevelSum(root), 3)

        # Test case 2: Maximum level sum is 7 (level 1)
        #   5
        #  / \
        # 2   3
        root = TreeNode(5)
        root.left = TreeNode(2)
        root.right = TreeNode(3)

        self.assertEqual(solution.maxLevelSum(root), 1)

        # Test case 3: Maximum level sum is -2 (level 2)
        #   1
        #  / \
        # 2    3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)

        self.assertEqual(solution.maxLevelSum(root), 2)

if __name__ == '__main__':
    unittest.main()
