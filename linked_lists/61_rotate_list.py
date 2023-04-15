import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: [ListNode], k: int) -> [ListNode]:

        # SECOND PASS - CIRCULAR CHAIN  O(2n)

        # edge cases
        if head == None: return None
        if k == 0: return head

        dummy = head
        l = 1  # track length

        while head.next:
            l += 1
            head = head.next

        k = k % l  # reduce k if > l
        l -= k  # actual rotations needed

        if k == 0: return dummy  # edge case

        head.next = dummy  # list is now circular

        # make rotations
        for _ in range(l): head = head.next

        ans = head.next  # new head
        head.next = None  # cut circle

        return ans

        # FIRST PASS - LIST OF NODES O(2n)
        # nodes = []

        # while head:
        #     nodes.append(head)
        #     head = head.next

        # l = len(nodes)

        # # edge cases
        # if nodes == []: return head
        # if (k == 0) or (k%l == 0): return nodes[0]

        # s = (k%l) * -1
        # start = nodes[s]
        # dummy = start

        # while start.next: start = start.next
        # start.next = nodes[0]

        # for _ in range(l-(k%l)): start = start.next

        # start.next = None

        # return dummy


class TestSolution(unittest.TestCase):

    def test_rotateRight(self):
        # Test case 1
        n1 = ListNode(1)
        n2 = ListNode(2)
        n3 = ListNode(3)
        n4 = ListNode(4)
        n5 = ListNode(5)

        n1.next = n2
        n2.next = n3
        n3.next = n4
        n4.next = n5

        s = Solution()
        result = s.rotateRight(n1, 2)

        self.assertEqual(result.val, 4)
        self.assertEqual(result.next.val, 5)
        self.assertEqual(result.next.next.val, 1)
        self.assertEqual(result.next.next.next.val, 2)
        self.assertEqual(result.next.next.next.next.val, 3)
        self.assertIsNone(result.next.next.next.next.next)

        # Test case 2
        n1 = ListNode(0)
        n2 = ListNode(1)
        n3 = ListNode(2)

        n1.next = n2
        n2.next = n3

        s = Solution()
        result = s.rotateRight(n1, 4)

        self.assertEqual(result.val, 2)
        self.assertEqual(result.next.val, 0)
        self.assertEqual(result.next.next.val, 1)
        self.assertIsNone(result.next.next.next)

        # Test case 3
        n1 = ListNode(1)
        n2 = ListNode(2)
        n3 = ListNode(3)
        n4 = ListNode(4)
        n5 = ListNode(5)

        n1.next = n2
        n2.next = n3
        n3.next = n4
        n4.next = n5

        s = Solution()
        result = s.rotateRight(n1, 0)

        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 2)
        self.assertEqual(result.next.next.val, 3)
        self.assertEqual(result.next.next.next.val, 4)
        self.assertEqual(result.next.next.next.next.val, 5)
        self.assertIsNone(result.next.next.next.next.next)

        # Test case 4
        n1 = None

        s = Solution()
        result = s.rotateRight(n1, 3)

        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
