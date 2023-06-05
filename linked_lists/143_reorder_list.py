import unittest
from typing import Optional

"""

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        second = prev

        first = head
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

        return head


def create_linked_list(nums):
    if not nums:
        return None
    head = ListNode(nums[0])
    current = head
    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next
    return head

def print_linked_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def run_tests():
    # Test case 1
    # Input: 1 -> 2 -> 3 -> 4
    # Output: 1 -> 4 -> 2 -> 3
    nums = [1, 2, 3, 4]
    linked_list = create_linked_list(nums)

    solution = Solution()
    solution.reorderList(linked_list)

    expected_output = [1, 4, 2, 3]
    assert print_linked_list(linked_list) == expected_output

    # Test case 2
    # Input: 1 -> 2 -> 3 -> 4 -> 5
    # Output: 1 -> 5 -> 2 -> 4 -> 3
    nums = [1, 2, 3, 4, 5]
    linked_list = create_linked_list(nums)

    solution = Solution()
    solution.reorderList(linked_list)

    expected_output = [1, 5, 2, 4, 3]
    assert print_linked_list(linked_list) == expected_output

    # Test case 3
    # Input: 1
    # Output: 1
    nums = [1]
    linked_list = create_linked_list(nums)

    solution = Solution()
    solution.reorderList(linked_list)

    expected_output = [1]
    assert print_linked_list(linked_list) == expected_output

    print("All tests pass")

run_tests()

