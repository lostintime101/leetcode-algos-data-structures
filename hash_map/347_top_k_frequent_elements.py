import unittest
from typing import List
import collections

"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = collections.defaultdict(dict)

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        return [i[0] for i in freq[:k]]


class TestSolution(unittest.TestCase):

    def test_topKFrequent(self):
        sol = Solution()

        # Test case 1
        nums = [1,1,1,2,2,3]
        k = 2
        expected_output = [1, 2]
        self.assertListEqual(sol.topKFrequent(nums, k), expected_output)

        # Test case 2
        nums = [1]
        k = 1
        expected_output = [1]
        self.assertListEqual(sol.topKFrequent(nums, k), expected_output)

        # Test case 3
        nums = [4,1,-1,2,-1,2,3]
        k = 2
        expected_output = [-1, 2]
        self.assertListEqual(sol.topKFrequent(nums, k), expected_output)


if __name__ == '__main__':
    unittest.main()
