import unittest
from collections import deque

"""

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ret_array, curr, prev = [], [], [root]

        while prev:
            for node in prev:
                if not node:
                    ret_array.append("null")
                else:
                    ret_array.append(str(node.val))
                    curr.append(node.left)
                    curr.append(node.right)
            prev = curr
            curr = []

        if ret_array != ["null"]:
            while ret_array[-1] == "null": ret_array.pop()

        ret_str = ""
        for n in ret_array: ret_str += n + ","
        ret_str = ret_str[:-1]
        return ret_str

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        data_array = deque(data.split(","))
        if data_array[0] == "null": return []

        root = TreeNode(int(data_array.popleft()))
        prev, curr = deque(), deque()
        prev.append(root)

        left, right = True, False

        while prev and data_array:

            val = data_array.popleft()
            new_node = None
            if val != "null": new_node = TreeNode(int(val))

            if new_node:
                if left: prev[0].left = new_node
                if right: prev[0].right = new_node
                curr.append(new_node)

            if left:
                left, right = False, True
            else:
                left, right = True, False
                prev.popleft()

            if not prev:
                prev = curr
                curr = deque()

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# Import the necessary classes and functions

class Codec:
    # The code for the serialize() and deserialize() methods

    # Unit tests for the Codec class
    class CodecTestCase(unittest.TestCase):
        def test_serialize_deserialize(self):
            # Create a sample binary tree
            root = TreeNode(1)
            root.left = TreeNode(2)
            root.right = TreeNode(3)
            root.left.left = TreeNode(4)
            root.left.right = TreeNode(5)
            root.right.left = TreeNode(6)
            root.right.right = TreeNode(7)

            # Create codec object
            codec = Codec()

            # Serialize the binary tree
            serialized = codec.serialize(root)

            # Deserialize the serialized string
            deserialized = codec.deserialize(serialized)

            # Verify that the deserialized tree matches the original tree
            self.assertEqual(deserialized.val, 1)
            self.assertEqual(deserialized.left.val, 2)
            self.assertEqual(deserialized.right.val, 3)
            self.assertEqual(deserialized.left.left.val, 4)
            self.assertEqual(deserialized.left.right.val, 5)
            self.assertEqual(deserialized.right.left.val, 6)
            self.assertEqual(deserialized.right.right.val, 7)

        def test_serialize_deserialize_empty_tree(self):
            # Create an empty binary tree
            root = None

            # Create codec object
            codec = Codec()

            # Serialize the binary tree
            serialized = codec.serialize(root)

            # Deserialize the serialized string
            deserialized = codec.deserialize(serialized)

            # Verify that the deserialized tree is None
            self.assertIsNone(deserialized)

        def test_serialize_deserialize_single_node(self):
            # Create a single-node binary tree
            root = TreeNode(1)

            # Create codec object
            codec = Codec()

            # Serialize the binary tree
            serialized = codec.serialize(root)

            # Deserialize the serialized string
            deserialized = codec.deserialize(serialized)

            # Verify that the deserialized tree matches the original tree
            self.assertEqual(deserialized.val, 1)
            self.assertIsNone(deserialized.left)
            self.assertIsNone(deserialized.right)


if __name__ == '__main__':
    unittest.main()

