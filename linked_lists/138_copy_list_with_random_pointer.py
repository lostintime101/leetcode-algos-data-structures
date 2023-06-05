import unittest
from typing import Optional

"""

A linked list of length n is given such that each node contains an additional random pointer, 
which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, 
where each new node has its value set to the value of its corresponding original node. 
Both the next and random pointer of the new nodes should point to new nodes in the copied list such that 
the pointers in the original list and copied list represent the same list state. 
None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, 
where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

Constraints:

0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list.

"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head: return None

        ret = Node(head.val)
        original, newHead = head, ret

        nodes, newNodes, count = {}, {}, 0

        # set up new list, store nodes
        while head:
            count += 1

            if head.next: newHead.next = Node(0)
            newHead.val = head.val

            if head.val in nodes:
                nodes[head.val].append([count, head])
                newNodes[newHead.val].append([count, newHead])
            else:
                nodes[head.val] = [[count, head]]
                newNodes[newHead.val] = [[count, newHead]]

            head, newHead = head.next, newHead.next

        head, newHead = original, ret

        # add random pointers
        while head:

            if head.random:
                val = head.random.val
                randomNode = head.random

                for node in nodes[val]:
                    if node[1] == randomNode: i = node[0]

                for node in newNodes[val]:
                    if node[0] == i: newHead.random = node[1]

            head, newHead = head.next, newHead.next

        return ret


def run_tests():
    # Test case 1
    # Input: 1 -> 2 -> None
    #        |---------^
    # Output: 1 -> 2 -> None
    #         |---------^
    node1 = Node(1)
    node2 = Node(2)
    node1.next = node2
    node1.random = node2
    node2.random = node2

    solution = Solution()
    copied_node = solution.copyRandomList(node1)

    assert copied_node.val == 1
    assert copied_node.next.val == 2
    assert copied_node.random.val == 2
    assert copied_node.next.random.val == 2
    assert copied_node.next.next is None
    assert copied_node.random.next is None

    # Test case 2
    # Input: 1 -> None
    # Output: 1 -> None
    node1 = Node(1)

    solution = Solution()
    copied_node = solution.copyRandomList(node1)

    assert copied_node.val == 1
    assert copied_node.next is None
    assert copied_node.random is None

    # Test case 3
    # Input: None
    # Output: None
    solution = Solution()
    copied_node = solution.copyRandomList(None)

    assert copied_node is None

    print("All tests pass")


run_tests()
