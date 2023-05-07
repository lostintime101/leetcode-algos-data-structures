import unittest

"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):

        # BETTER BUT SLOW

        if not list1 and not list2: return list1

        start = ret = ListNode(0)

        while list1 and list2:

            if list1.val <= list2.val:
                start.val = list1.val
                list1 = list1.next
            else:
                start.val = list2.val
                list2 = list2.next

            start.next = ListNode(0)
            start = start.next

        if list1:
            start.val = list1.val
            start.next = list1.next
        else:
            start.val = list2.val
            start.next = list2.next

        return ret

        # WORKS BUT LONG & COMPLEX
        # vals = []

        # while list1 or list2:
        #     if list1 and list2:
        #         if list1.val <= list2.val:
        #             vals.append(list1.val)
        #             list1 = list1.next
        #         else:
        #             vals.append(list2.val)
        #             list2 = list2.next
        #     elif list1:
        #         vals.append(list1.val)
        #         list1 = list1.next
        #     else:
        #         vals.append(list2.val)
        #         list2 = list2.next

        # if len(vals) == 0: return None
        # list3 = ListNode(vals[-1])
        # if len(vals) ==1: return list3

        # for i in range(len(vals)-2, -1, -1):
        #     list3 = ListNode(vals[i], list3)

        # return list3



def test_mergeTwoLists():
    # Test case 1: empty lists
    assert Solution().mergeTwoLists(None, None) == None

    # Test case 2: list1 is empty
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node2.next = node3
    merged_list = Solution().mergeTwoLists(None, node2)
    assert merged_list.val == 2
    assert merged_list.next.val == 3
    assert merged_list.next.next == None

    # Test case 3: list2 is empty
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    merged_list = Solution().mergeTwoLists(node1, None)
    assert merged_list.val == 1
    assert merged_list.next.val == 2
    assert merged_list.next.next == None

    # Test case 4: both lists have elements
    node1a = ListNode(1)
    node2a = ListNode(2)
    node3a = ListNode(4)
    node1a.next = node2a
    node2a.next = node3a
    node1b = ListNode(1)
    node2b = ListNode(3)
    node3b = ListNode(4)
    node1b.next = node2b
    node2b.next = node3b
    merged_list = Solution().mergeTwoLists(node1a, node1b)
    assert merged_list.val == 1
    assert merged_list.next.val == 1
    assert merged_list.next.next.val == 2
    assert merged_list.next.next.next.val == 3
    assert merged_list.next.next.next.next.val == 4
    assert merged_list.next.next.next.next.next.val == 4
    assert merged_list.next.next.next.next.next.next == None


def main():
    test_mergeTwoLists()
    print("All tests passed")


if __name__ == "__main__":
    main()

