import unittest
from typing import List


"""
You are given an array happiness of length n, and a positive integer k.

There are n children standing in a queue, where the ith child has happiness value happiness[i]. You want to select k children from these n children in k turns.

In each turn, when you select a child, the happiness value of all the children that have not been selected till now decreases by 1. Note that the happiness value cannot become negative and gets decremented only if it is positive.

Return the maximum sum of the happiness values of the selected children you can achieve by selecting k children.

Constraints:

1 <= n == happiness.length <= 2 * 105
1 <= happiness[i] <= 108
1 <= k <= n

"""


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:

        array = sorted(happiness)[-k:]
        array = array[::-1]
        for i in range(len(array)):
            array[i] -= i
            if array[i] < 0:
                array[i] = 0

        return sum(array)


import unittest
from typing import List


# Assuming the Solution class and maximumHappinessSum function are defined in the same file
# or you can import the class from the file where it is defined.

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        array = sorted(happiness)[-k:]
        array = array[::-1]
        for i in range(len(array)):
            array[i] -= i
            if array[i] < 0:
                array[i] = 0
        return sum(array)


class TestMaximumHappinessSum(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        happiness = [3, 5, 1, 4, 2]
        k = 3
        expected = 9  # This can be calculated manually or through some other function
        result = self.solution.maximumHappinessSum(happiness, k)
        self.assertEqual(result, expected)

    def test_example_2(self):
        happiness = [10, 20, 30, 40, 50]
        k = 2
        expected = 89  # This can be calculated manually or through some other function
        result = self.solution.maximumHappinessSum(happiness, k)
        self.assertEqual(result, expected)

    def test_all_positive_happiness(self):
        happiness = [10, 20, 30, 40, 50]
        k = 3
        expected = 117  # This can be calculated manually or through some other function
        result = self.solution.maximumHappinessSum(happiness, k)
        self.assertEqual(result, expected)

    def test_all_negative_happiness(self):
        happiness = [-1, -2, -3, -4, -5]
        k = 3
        expected = 0  # All values will be zero after processing, so sum will be zero
        result = self.solution.maximumHappinessSum(happiness, k)
        self.assertEqual(result, expected)

    def test_mixed_happiness(self):
        happiness = [3, -1, 5, 2, 4, -3]
        k = 4
        expected = 9  # This can be calculated manually or through some other function
        result = self.solution.maximumHappinessSum(happiness, k)
        self.assertEqual(result, expected)

    def test_empty_happiness(self):
        happiness = []
        k = 0
        expected = 0  # With no values, sum should be zero
        result = self.solution.maximumHappinessSum(happiness, k)
        self.assertEqual(result, expected)

    def test_one_element_happiness(self):
        happiness = [5]
        k = 1
        expected = 5  # Only one element, so sum is the element itself
        result = self.solution.maximumHappinessSum(happiness, k)
        self.assertEqual(result, expected)

    def test_k_equals_happiness_length(self):
        happiness = [4, 6, 8, 2, 1, 9, 5]
        k = len(happiness)
        expected = 22  # Calculate sum from all elements minus the adjustments
        result = self.solution.maximumHappinessSum(happiness, k)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()


