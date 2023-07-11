import unittest
from typing import List

"""

Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

Constraints:

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        ret = []
        blocked = set()

        # find all relevant vals downstream from this node
        def find_vals_downstream(nod, curr):

            # stops us going back the way we came
            if nod.val in blocked: return
            blocked.add(nod.val)

            if curr == 0:
                ret.append(nod.val)
                return

            curr -= 1
            if nod.left: find_vals_downstream(nod.left, curr)
            if nod.right: find_vals_downstream(nod.right, curr)

        # go back up parent chain as far as k allows us
        def k_distances_from_target(path_array):
            n = 0

            while path_array and (k - n > -1):
                new = path_array.pop()
                find_vals_downstream(new, k - n)
                n += 1
            return

        # returns the target node and all the parent nodes leading to it
        def find_target(path: List[TreeNode], found: bool):

            if found: return
            if path[-1].val == target.val:
                k_distances_from_target(path)
                found = True
                return path

            if path[-1].left:
                path.append(path[-1].left)
                find_target(path[::], found)
                path.pop()

            if path[-1].right:
                path.append(path[-1].right)
                find_target(path[::], found)
                path.pop()

        find_target([root], False)

        return ret




class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_distanceK(self):
        # Create the binary tree
        #      3
        #     / \
        #    5   1
        #   / \   \
        #  6   2   0
        #     / \
        #    7   4
        root = TreeNode(3)
        root.left = TreeNode(5)
        root.right = TreeNode(1)
        root.left.left = TreeNode(6)
        root.left.right = TreeNode(2)
        root.left.right.left = TreeNode(7)
        root.left.right.right = TreeNode(4)
        root.right.right = TreeNode(0)

        target = root.left  # Node with value 5
        k = 2

        expected_output = [7, 4, 1]  # Nodes at distance 2 from target

        result = self.solution.distanceK(root, target, k)
        self.assertEqual(result, expected_output)

        # Test with different target and k values
        target = root  # Node with value 3
        k = 3

        expected_output = [7, 4]  # Nodes at distance 3 from target

        result = self.solution.distanceK(root, target, k)
        self.assertEqual(result, expected_output)

        # Test with target being a leaf node
        target = root.right.right  # Node with value 0
        k = 2

        expected_output = [3]  # Nodes at distance 2 from target

        result = self.solution.distanceK(root, target, k)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
