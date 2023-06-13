import unittest
from typing import Optional

"""

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        head2 = head

        while head2 and head2.next:
            if head2.next.val == head2.val:
                head2.next = head2.next.next
            else:
                head2 = head2.next

        return head


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def createLinkedList(self, nums):
        # Create a linked list from a list of values
        dummy = ListNode()
        current = dummy
        for num in nums:
            current.next = ListNode(num)
            current = current.next
        return dummy.next

    def linkedListToList(self, head):
        # Convert a linked list to a list of values
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def test_deleteDuplicates(self):
        # Test case 1: No duplicates
        nums = [1, 2, 3, 4, 5]
        head = self.createLinkedList(nums)
        expected = [1, 2, 3, 4, 5]
        result = self.solution.deleteDuplicates(head)
        self.assertEqual(self.linkedListToList(result), expected)

        # Test case 2: Duplicates at the beginning
        nums = [1, 1, 2, 3, 4, 5]
        head = self.createLinkedList(nums)
        expected = [1, 2, 3, 4, 5]
        result = self.solution.deleteDuplicates(head)
        self.assertEqual(self.linkedListToList(result), expected)

        # Test case 3: Duplicates in the middle
        nums = [1, 2, 2, 3, 4, 5]
        head = self.createLinkedList(nums)
        expected = [1, 2, 3, 4, 5]
        result = self.solution.deleteDuplicates(head)
        self.assertEqual(self.linkedListToList(result), expected)

        # Test case 4: Duplicates at the end
        nums = [1, 2, 3, 4, 5, 5]
        head = self.createLinkedList(nums)
        expected = [1, 2, 3, 4, 5]
        result = self.solution.deleteDuplicates(head)
        self.assertEqual(self.linkedListToList(result), expected)

        # Test case 5: All duplicates
        nums = [1, 1, 1, 1, 1]
        head = self.createLinkedList(nums)
        expected = [1]
        result = self.solution.deleteDuplicates(head)
        self.assertEqual(self.linkedListToList(result), expected)

if __name__ == '__main__':
    unittest.main()
