import unittest
from typing import List


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """

        total_nodes = 0
        head2 = head

        while head2:
            total_nodes += 1
            head2 = head2.next

        higher = (total_nodes // k) + 1
        high_count = total_nodes % k

        ans = []

        for i in range(1, k + 1):

            if i <= high_count:
                loops = higher - 1
            else:
                loops = higher - 2

            start = head
            for j in range(loops):

                if head:
                    head = head.next
                else:
                    head = None

            if head:
                next_start = head.next
            else:
                next_start = None

            if head: head.next = None

            ans.append(start)
            head = next_start

        return ans
