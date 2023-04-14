import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):

        # METHOD 1
        # num1, num2 = [], []

        # while l1:
        #     num1.append(l1.val)
        #     l1 = l1.next
        # while l2:
        #     num2.append(l2.val)
        #     l2 = l2.next

        # num1 = int("".join([str(i) for i in num1][::-1]))
        # num2 = int("".join([str(i) for i in num2][::-1]))

        # num1 += num2
        # num1 = str(num1)

        # ans = ListNode(num1[0])

        # for i in range(1, len(num1)):

        #     ans = ListNode(num1[i], ans)

        # return ans

        # METHOD 2

        ans = ListNode()
        ans2 = ans
        carry = 0

        while l1 or l2 or carry:

            ans.next = ListNode()
            ans = ans.next

            a, b = 0, 0

            if l1:
                a = l1.val
                l1 = l1.next

            if l2:
                b = l2.val
                l2 = l2.next

            a = a + b + carry
            carry = 0

            carry = a // 10
            a = a % 10

            ans.val = a

        return ans2.next


def compare_linked_lists(l1, l2):
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next
    return l1 is None and l2 is None


class TestSolution(unittest.TestCase):
    def test_addTwoNumbers(self):
        # Test case 1
        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(4)))
        expected_output = ListNode(7, ListNode(0, ListNode(8)))
        solution = Solution()
        self.assertTrue(compare_linked_lists(solution.addTwoNumbers(l1, l2), expected_output))

        # Test case 2
        l1 = ListNode(0)
        l2 = ListNode(0)
        expected_output = ListNode(0)
        solution = Solution()
        self.assertTrue(compare_linked_lists(solution.addTwoNumbers(l1, l2), expected_output))

        # Test case 3
        l1 = ListNode(9, ListNode(9, ListNode(9)))
        l2 = ListNode(9, ListNode(9))
        expected_output = ListNode(8, ListNode(9, ListNode(0, ListNode(1))))
        solution = Solution()
        self.assertTrue(compare_linked_lists(solution.addTwoNumbers(l1, l2), expected_output))


if __name__ == '__main__':
    unittest.main()
