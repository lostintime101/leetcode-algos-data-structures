import unittest
from typing import List
from collections import Counter

"""

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000

"""

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        freq_list = []

        for v in freq.values(): freq_list.append(v)

        return len(set(freq_list)) == len(freq_list)



# Unit tests
class TestSolution(unittest.TestCase):

    def test_uniqueOccurrences(self):
        # Test case 1: Empty list
        solution = Solution()
        self.assertEqual(solution.uniqueOccurrences([]), True)

        # Test case 2: List with unique elements
        solution = Solution()
        self.assertEqual(solution.uniqueOccurrences([1, 2, 3, 4, 5]), False)

        # Test case 3: List with duplicate elements, but all occurrences are unique
        solution = Solution()
        self.assertEqual(solution.uniqueOccurrences([1, 1, 2, 2, 3, 3]), False)

        # Test case 4: List with duplicate elements and some occurrences are not unique
        solution = Solution()
        self.assertEqual(solution.uniqueOccurrences([1, 1, 2, 2, 2, 3]), True)

        # Test case 5: List with negative elements and duplicate occurrences
        solution = Solution()
        self.assertEqual(solution.uniqueOccurrences([-1, -1, 2, 2, 2, 3, 3]), False)


if __name__ == '__main__':
    unittest.main()
