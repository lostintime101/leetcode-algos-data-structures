import unittest
from typing import List

"""

You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.

Constraints:

n == leftChild.length == rightChild.length
1 <= n <= 104
-1 <= leftChild[i], rightChild[i] <= n - 1

"""

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        leaves = []
        parents = {}

        for i in range(len(leftChild)):

            if leftChild[i] == -1 and rightChild[i] == -1:
                leaves.append(i)
                continue

            if leftChild[i] != -1:
                if parents.get(leftChild[i]) == None:
                    parents[leftChild[i]] = i
                else:
                    return False

            if rightChild[i] != -1:
                if parents.get(rightChild[i]) == None:
                    parents[rightChild[i]] = i
                else:
                    return False

        if not leaves: return False

        origin = None
        count = len(leaves)

        while leaves:
            new_leaves = []

            for leave in leaves:

                if parents.get(leave) == None:
                    if origin == None: origin = leave
                    if origin != leave: return False

                else:
                    new_leaves.append(parents[leave])

            leaves = new_leaves
            count += len(new_leaves)

        return count >= n


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_binary_tree(self):
        n = 3
        leftChild = [1, -1, -1]
        rightChild = [2, -1, -1]
        self.assertTrue(self.solution.validateBinaryTreeNodes(n, leftChild, rightChild))

    def test_invalid_binary_tree_with_duplicate_parent(self):
        n = 3
        leftChild = [1, -1, -1]
        rightChild = [1, -1, -1]
        self.assertFalse(self.solution.validateBinaryTreeNodes(n, leftChild, rightChild))

    def test_invalid_binary_tree_with_cycle(self):
        n = 3
        leftChild = [1, -1, 0]
        rightChild = [-1, -1, -1]
        self.assertTrue(self.solution.validateBinaryTreeNodes(n, leftChild, rightChild))

    def test_invalid_binary_tree_with_multiple_roots(self):
        n = 3
        leftChild = [-1, 0, -1]
        rightChild = [-1, 1, -1]
        self.assertFalse(self.solution.validateBinaryTreeNodes(n, leftChild, rightChild))

    def test_invalid_binary_tree_with_no_root(self):
        n = 3
        leftChild = [-1, -1, -1]
        rightChild = [-1, -1, -1]
        self.assertFalse(self.solution.validateBinaryTreeNodes(n, leftChild, rightChild))


if __name__ == "__main__":
    unittest.main()
