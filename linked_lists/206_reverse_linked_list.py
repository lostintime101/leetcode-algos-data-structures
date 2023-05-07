import unittest

"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):

        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

        # # edge case
        # if head == None: return head

        # # go through linkedlist, collect vals
        # vals = []
        # while head:
        #     vals.append(head.val)
        #     head = head.next

        # # start new linkedlist with 1st val
        # head = ListNode(vals[0])

        # # create linkedlist
        # for i in range(1, len(vals)):
        #     head = ListNode(vals[i], head)

        # return head


def test_reverseList():
    # Test case 1: empty list
    assert Solution().reverseList(None) == None

    # Test case 2: list with one element
    node1 = ListNode(1)
    assert Solution().reverseList(node1) == node1

    # Test case 3: list with multiple elements
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    reversed_list = Solution().reverseList(node1)
    assert reversed_list.val == 3
    assert reversed_list.next.val == 2
    assert reversed_list.next.next.val == 1
    assert reversed_list.next.next.next == None


def main():
    test_reverseList()
    print("All tests passed")

if __name__ == "__main__":
    main()