import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:

        # STEP 1: CREATE REVERSE LINKED LISTS

        l1a = ListNode(l1.val)
        l1 = l1.next

        while l1:
            l1a = ListNode(l1.val, l1a)
            l1 = l1.next

        l2a = ListNode(l2.val)
        l2 = l2.next

        while l2:
            l2a = ListNode(l2.val, l2a)
            l2 = l2.next

        # STEP 2: ADD THE LISTS TOGETHER

        carry = 0  # if ans above 9 (e.g. 5 + 7 = 12, carry=1)
        ans = None

        while l1a or l2a or carry:

            val = 0

            if l1a:
                val += l1a.val
                l1a = l1a.next
            if l2a:
                val += l2a.val
                l2a = l2a.next

            if carry: val += carry

            val2 = val % 10
            carry = val // 10

            ans = ListNode(val2, ans)

        return ans


class TestSolution(unittest.TestCase):

    def createLinkedList(self, lst):
        """
        Utility function to create a linked list from a list of values.
        """
        head = ListNode(lst[0])
        current = head
        for val in lst[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def createListFromLinkedList(self, head):
        """
        Utility function to create a list from a linked list.
        """
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        return lst

    def test_addTwoNumbers(self):
        sol = Solution()

        # test case 1
        l1 = self.createLinkedList([2, 4, 3])
        l2 = self.createLinkedList([5, 6, 4])
        expected = [8, 0, 7]
        actual = self.createListFromLinkedList(sol.addTwoNumbers(l1, l2))
        self.assertEqual(actual, expected)

        # test case 2
        l1 = self.createLinkedList([0])
        l2 = self.createLinkedList([0])
        expected = [0]
        actual = self.createListFromLinkedList(sol.addTwoNumbers(l1, l2))
        self.assertEqual(actual, expected)

        # test case 3
        l1 = self.createLinkedList([9, 9, 9, 9, 9, 9, 9])
        l2 = self.createLinkedList([9, 9, 9, 9])
        expected = [1, 0, 0, 0, 9, 9, 9, 8]
        actual = self.createListFromLinkedList(sol.addTwoNumbers(l1, l2))
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()