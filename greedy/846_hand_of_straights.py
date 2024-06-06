import unittest
from typing import List

"""

Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

Constraints:

1 <= hand.length <= 104
0 <= hand[i] <= 109
1 <= groupSize <= hand.length

"""

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        N = len(hand)
        counts = sorted(hand)

        for (start, v) in enumerate(counts):

            if v == -1: continue

            counts[start] = -1
            count = 1
            curr_v = v + 1
            end = start + 1

            while groupSize > count and end < N:

                if counts[end] == curr_v:
                    counts[end] = -1
                    count += 1
                    curr_v += 1
                    end += 1
                else:
                    end += 1

            if count != groupSize:
                return False

        return True


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
        groupSize = 3
        self.assertTrue(self.solution.isNStraightHand(hand, groupSize))

    def test_example2(self):
        hand = [1, 2, 3, 4, 5]
        groupSize = 4
        self.assertFalse(self.solution.isNStraightHand(hand, groupSize))

    def test_example3(self):
        hand = [1, 2, 3, 4, 5, 6]
        groupSize = 2
        self.assertTrue(self.solution.isNStraightHand(hand, groupSize))

    def test_single_group(self):
        hand = [1, 2, 3]
        groupSize = 3
        self.assertTrue(self.solution.isNStraightHand(hand, groupSize))

    def test_incomplete_group(self):
        hand = [1, 2, 3, 4]
        groupSize = 3
        self.assertFalse(self.solution.isNStraightHand(hand, groupSize))

    def test_multiple_groups(self):
        hand = [1, 2, 3, 3, 4, 5]
        groupSize = 3
        self.assertTrue(self.solution.isNStraightHand(hand, groupSize))

    def test_no_possible_groups(self):
        hand = [1, 2, 3, 5, 6, 7]
        groupSize = 3
        self.assertTrue(self.solution.isNStraightHand(hand, groupSize))

    def test_empty_hand(self):
        hand = []
        groupSize = 1
        self.assertTrue(self.solution.isNStraightHand(hand, groupSize))

    def test_group_size_greater_than_hand(self):
        hand = [1, 2, 3]
        groupSize = 4
        self.assertFalse(self.solution.isNStraightHand(hand, groupSize))

    def test_repeating_elements(self):
        hand = [1, 2, 3, 1, 2, 3]
        groupSize = 3
        self.assertTrue(self.solution.isNStraightHand(hand, groupSize))


if __name__ == '__main__':
    unittest.main()
