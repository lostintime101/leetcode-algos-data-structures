import unittest
import heapq

"""

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
You must solve it in O(n) time complexity.

Constraints:
1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104

"""

class Solution:
    def findKthLargest(self, nums: [int], k: int):

        # 1 USE HEAP

        heapq.heapify(nums)

        for _ in range(len(nums)- k): heapq.heappop(nums)

        return heapq.heappop(nums)

        # 2 USE SORT

        # nums.sort()

        # return nums[len(nums) - k]


class TestFindKthLargest(unittest.TestCase):

    def test_heap_solution(self):
        s = Solution()
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        result = s.findKthLargest(nums, k)
        self.assertEqual(result, 5)

    def test_sort_solution(self):
        s = Solution()
        nums = [3, 2, 1, 5, 6, 4]
        k = 4
        result = s.findKthLargest(nums, k)
        self.assertEqual(result, 3)

    def test_empty_list(self):
        s = Solution()
        nums = []
        k = 1
        self.assertRaises(IndexError, s.findKthLargest, nums, k)


if __name__ == '__main__':
    unittest.main()
