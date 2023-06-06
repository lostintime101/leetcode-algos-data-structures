import unittest
from typing import Optional, List

"""

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000


"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        ret, curr_level = [], [root]

        while curr_level:
            new_level, values = [], []
            for node in curr_level:
                if node:
                    values.append(node.val)
                    new_level.extend([node.left, node.right])
            if values: ret.append(values)
            curr_level = new_level

        return ret

        # if root == None: return None

        # layer = [root]
        # next_layer, layer_vals, ans = [], [], []

        # while layer:

        #     for i in layer:

        #         layer_vals.append(i.val)

        #         if i.left:
        #             next_layer.append(i.left)
        #         if i.right:
        #             next_layer.append(i.right)

        #     ans.append(layer_vals)
        #     layer_vals = []

        #     layer = next_layer
        #     next_layer = []

        # return ans


class LevelOrderTests(unittest.TestCase):
    def test_levelOrder(self):
        solution = Solution()

        # Test case 1: Empty tree
        root = None
        expected_output = []
        self.assertEqual(solution.levelOrder(root), expected_output)

        # Test case 2: Tree with a single node
        root = TreeNode(5)
        expected_output = [[5]]
        self.assertEqual(solution.levelOrder(root), expected_output)

        # Test case 3: Tree with multiple levels and nodes
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        expected_output = [[3], [9, 20], [15, 7]]
        self.assertEqual(solution.levelOrder(root), expected_output)

        # Additional test cases...
        # You can add more test cases to further validate the solution

if __name__ == '__main__':
    unittest.main()
