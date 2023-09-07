import unittest

"""

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left == right: return head

        first_node = head

        for _ in range(left - 2): head = head.next

        first_section = head
        curr = head.next
        prev = None

        if left == 1:
            first_section = None
            curr = head

        for _ in range(right - left):
            new = curr.next
            curr.next = prev
            prev = curr
            curr = new

        final_section = curr.next
        curr.next = prev
        if first_section:
            first_section.next = curr
        else:
            first_section = curr

        head = first_node

        while head.next: head = head.next
        head.next = final_section

        if left == 1: return curr

        return first_node


class TestReverseBetween(unittest.TestCase):

    def create_linked_list(self, values):
        """
        Helper function to create a linked list from a list of values.
        """
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def linked_list_to_list(self, head):
        """
        Helper function to convert a linked list into a list.
        """
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def test_reverse_between(self):
        solution = Solution()

        # Test Case 1
        head = self.create_linked_list([1, 2, 3, 4, 5])
        left = 2
        right = 4
        expected_output = [1, 4, 3, 2, 5]
        result = solution.reverseBetween(head, left, right)
        self.assertEqual(self.linked_list_to_list(result), expected_output)

        # Test Case 2
        head = self.create_linked_list([1, 2, 3, 4, 5])
        left = 1
        right = 5
        expected_output = [5, 4, 3, 2, 1]
        result = solution.reverseBetween(head, left, right)
        self.assertEqual(self.linked_list_to_list(result), expected_output)

        # Test Case 3
        head = self.create_linked_list([5, 4, 3, 2, 1])
        left = 2
        right = 4
        expected_output = [5, 2, 3, 4, 1]
        result = solution.reverseBetween(head, left, right)
        self.assertEqual(self.linked_list_to_list(result), expected_output)


if __name__ == '__main__':
    unittest.main()
