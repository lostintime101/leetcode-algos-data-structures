import unittest

"""

You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure indicate the result:


Build the result list and return its head.

Constraints:

3 <= list1.length <= 104
1 <= a <= b < list1.length - 1
1 <= list2.length <= 104

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        head = list1

        for _ in range(a - 1):
            head = head.next

        new = head.next

        for _ in range((b - a) + 1):
            new = new.next

        head.next = list2

        while head.next:
            head = head.next

        head.next = new

        return list1


class TestSolution(unittest.TestCase):
    def test_mergeInBetween_case1(self):
        # Creating the input lists
        list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        list2 = ListNode(6, ListNode(7, ListNode(8)))

        # Merging lists
        solution = Solution()
        result = solution.mergeInBetween(list1, 1, 3, list2)

        # Asserting the result
        expected_result = ListNode(1, ListNode(6, ListNode(7, ListNode(8, ListNode(4, ListNode(5))))))
        self.assertEqual(result.val, expected_result.val)
        self.assertEqual(result.next.val, expected_result.next.val)
        self.assertEqual(result.next.next.val, expected_result.next.next.val)
        self.assertEqual(result.next.next.next.val, expected_result.next.next.next.val)
        self.assertEqual(result.next.next.next.next.val, expected_result.next.next.next.next.val)
        self.assertEqual(result.next.next.next.next.next.val, expected_result.next.next.next.next.next.val)
        self.assertEqual(result.next.next.next.next.next.next, expected_result.next.next.next.next.next.next)

    def test_mergeInBetween_case2(self):
        # Creating the input lists
        list1 = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
        list2 = ListNode(5, ListNode(6, ListNode(7)))

        # Merging lists
        solution = Solution()
        result = solution.mergeInBetween(list1, 0, 2, list2)

        # Asserting the result
        expected_result = ListNode(0, ListNode(5, ListNode(6, ListNode(7, ListNode(3, ListNode(4))))))
        self.assertEqual(result.val, expected_result.val)
        self.assertEqual(result.next.val, expected_result.next.val)
        self.assertEqual(result.next.next.val, expected_result.next.next.val)
        self.assertEqual(result.next.next.next.val, expected_result.next.next.next.val)
        self.assertEqual(result.next.next.next.next.val, expected_result.next.next.next.next.val)
        self.assertEqual(result.next.next.next.next.next.val, expected_result.next.next.next.next.next.val)
        self.assertEqual(result.next.next.next.next.next.next, expected_result.next.next.next.next.next.next)

    def test_mergeInBetween_case3(self):
        # Creating the input lists
        list1 = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))
        list2 = ListNode(6, ListNode(7, ListNode(8)))

        # Merging lists
        solution = Solution()
        result = solution.mergeInBetween(list1, 2, 4, list2)

        # Asserting the result
        expected_result = ListNode(0, ListNode(1, ListNode(6, ListNode(7, ListNode(8, ListNode(5)))))))
        self.assertEqual(result.val, expected_result.val)
        self.assertEqual(result.next.val, expected_result.next.val)
        self.assertEqual(result.next.next.val, expected_result.next.next.val)
        self.assertEqual(result.next.next.next.val, expected_result.next.next.next.val)
        self.assertEqual(result.next.next.next.next.val, expected_result.next.next.next.next.val)
        self.assertEqual(result.next.next.next.next.next.val, expected_result.next.next.next.next.next.val)
        self.assertEqual(result.next.next.next.next.next.next, expected_result.next.next.next.next.next.next)

    def test_mergeInBetween_case4(self):
        # Creating the input lists
        list1 = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4))))))
        list2 = None

        # Merging lists
        solution = Solution()
        result = solution.mergeInBetween(list1, 1, 3, list2)

        # Asserting the result
        expected_result = ListNode(0, ListNode(4))
        self.assertEqual(result.val, expected_result.val)
        self.assertEqual(result.next.val, expected_result.next.val)
        self.assertEqual(result.next.next, expected_result.next.next)


if __name__ == '__main__':
    unittest.main()
