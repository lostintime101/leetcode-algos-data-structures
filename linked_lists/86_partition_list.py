import unittest
from typing import Optional

"""

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        if not head: return None
        part1, part2 = head, head

        if part1.val >= x: part1 = None
        while part1 and (part1.val < x) and part1.next and (part1.next.val < x):
            part1 = part1.next

        if part1:
            part2 = part1.next
            part1.next = None

        part1head, part2head = head, part2

        while part2:
            if part2.next and (part2.next.val < x):

                cut = part2.next
                part2.next = part2.next.next
                cut.next = None

                if part1:
                    part1.next = cut
                    part1 = part1.next

                else:
                    part1 = cut
                    part1head = part1

            else:
                part2 = part2.next

        if not part1: return head

        part1.next = part2head

        return part1head


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def create_linked_list(self, values):
        dummy = ListNode()
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    def linked_list_to_list(self, head):
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        return values

    def test_partition(self):
        # Test case 1
        head = self.create_linked_list([1, 4, 3, 2, 5, 2])
        x = 3
        expected_output = [1, 2, 2, 4, 3, 5]
        result = self.solution.partition(head, x)
        self.assertEqual(self.linked_list_to_list(result), expected_output)

        # Test case 2
        head = self.create_linked_list([2, 1])
        x = 2
        expected_output = [1, 2]
        result = self.solution.partition(head, x)
        self.assertEqual(self.linked_list_to_list(result), expected_output)

        # Test case 3
        head = self.create_linked_list([3, 1, 2])
        x = 3
        expected_output = [1, 2, 3]
        result = self.solution.partition(head, x)
        self.assertEqual(self.linked_list_to_list(result), expected_output)


if __name__ == '__main__':
    unittest.main()
