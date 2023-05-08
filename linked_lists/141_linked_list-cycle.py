import unittest

"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:

        slow, fast = head, head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast: return True

        return False


class TestSolution(unittest.TestCase):

    def test_no_cycle(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)

        node1.next = node2
        node2.next = node3

        solution = Solution()
        result = solution.hasCycle(node1)
        self.assertEqual(result, False)

    def test_cycle(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)

        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node2

        solution = Solution()
        result = solution.hasCycle(node1)
        self.assertEqual(result, True)

    def test_single_node_cycle(self):
        node1 = ListNode(1)
        node1.next = node1

        solution = Solution()
        result = solution.hasCycle(node1)
        self.assertEqual(result, True)

    def test_empty_list(self):
        solution = Solution()
        result = solution.hasCycle(None)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
