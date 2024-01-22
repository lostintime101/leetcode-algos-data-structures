import unittest
from collections import Counter
from typing import List

"""

You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

Constraints:

2 <= nums.length <= 104
1 <= nums[i] <= 104

"""


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        freq = Counter(nums)
        ans = [0, 0]

        for i in range(1, len(nums) + 1):

            if not freq[i]: ans[1] = i
            if freq[i] == 2: ans[0] = i

        return ans


class TestSolution(unittest.TestCase):

    def test_findErrorNums(self):
        solution = Solution()

        # Test case 1: Example case
        nums1 = [1, 2, 2, 4]
        self.assertEqual(solution.findErrorNums(nums1), [2, 3])

        # Test case 2: All elements are the same
        nums2 = [3, 3, 3, 3]
        self.assertEqual(solution.findErrorNums(nums2), [0, 4])

        # Test case 3: Missing and repeated elements
        nums3 = [1, 2, 2, 3, 4, 5]
        self.assertEqual(solution.findErrorNums(nums3), [2, 6])

        # Test case 4: All elements from 1 to 10, with 5 repeated
        nums4 = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
        self.assertEqual(solution.findErrorNums(nums4), [5, 11])


if __name__ == '__main__':
    unittest.main()
