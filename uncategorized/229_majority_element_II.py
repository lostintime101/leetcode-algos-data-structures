from collections import Counter
from typing import List
import unittest

"""

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109

"""


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [k for k, v in dict(Counter(nums)).items() if v > (len(nums) // 3)]


class TestMajorityElement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_majorityElement(self):
        # Test case 1: Input with a majority element
        nums1 = [3, 3, 4, 2, 2, 3, 7, 3, 3]
        self.assertEqual(self.solution.majorityElement(nums1), [3])

        # Test case 2: Input with multiple majority elements
        nums2 = [1, 2, 2, 1, 3, 2, 1, 3]
        self.assertEqual(set(self.solution.majorityElement(nums2)), {1, 2})

        # Test case 3: Input with no majority element
        nums3 = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.majorityElement(nums3), [])

        # Test case 4: Edge case with an empty input list
        nums4 = []
        self.assertEqual(self.solution.majorityElement(nums4), [])

        # Test case 5: Input with one element
        nums5 = [5]
        self.assertEqual(self.solution.majorityElement(nums5), [5])


if __name__ == '__main__':
    unittest.main()
