import unittest
from typing import Optional

"""

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Constraints:

The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        if not head: return None

        while head and head.val == val: head = head.next

        head2 = head

        while head2 and head2.next:

            while head2.next and head2.next.val == val:
                head2.next = head2.next.next

            head2 = head2.next

        return head



class SolutionTests(unittest.TestCase):
    def test_removeElements(self):
        # Test case 1: Remove all occurrences of 2
        # Input: 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 2
        # Output: 1 -> 6 -> 3 -> 4 -> 5
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(6)
        head.next.next.next = ListNode(3)
        head.next.next.next.next = ListNode(4)
        head.next.next.next.next.next = ListNode(5)
        head.next.next.next.next.next.next = ListNode(2)

        solution = Solution()
        result = solution.removeElements(head, 2)

        expected = [1, 6, 3, 4, 5]
        self.assertListEqual(self.get_linked_list_values(result), expected)

    def get_linked_list_values(self, head):
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        return values


if __name__ == '__main__':
    unittest.main()
