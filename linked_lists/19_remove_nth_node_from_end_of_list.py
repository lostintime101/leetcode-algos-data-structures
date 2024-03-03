import unittest
from typing import Optional

"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        N = 0
        curr = head
        while curr:
            N += 1
            curr = curr.next

        N = N - n

        if N == 0:
            head = head.next
        curr = head
        count = 0

        while curr:
            count += 1
            if count == N:
                curr.next = curr.next.next
            curr = curr.next

        return head


class TestSolution(unittest.TestCase):
    def create_linked_list(self, values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def linked_list_to_list(self, head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def test_removeNthFromEnd(self):
        solution = Solution()

        # Test case 1
        head1 = self.create_linked_list([1, 2, 3, 4, 5])
        result1 = solution.removeNthFromEnd(head1, 2)
        self.assertEqual(self.linked_list_to_list(result1), [1, 2, 3, 5])

        # Test case 2
        head2 = self.create_linked_list([1, 2, 3, 4, 5])
        result2 = solution.removeNthFromEnd(head2, 1)
        self.assertEqual(self.linked_list_to_list(result2), [1, 2, 3, 4])

        # Test case 3
        head3 = self.create_linked_list([1, 2, 3, 4, 5])
        result3 = solution.removeNthFromEnd(head3, 5)
        self.assertEqual(self.linked_list_to_list(result3), [2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
