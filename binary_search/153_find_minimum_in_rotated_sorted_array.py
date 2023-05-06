import unittest

"""

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.

"""

class Solution:
    def findMin(self, nums: [int]) -> int:

        l, r = 0, len(nums)-1
        start = nums[0]

        while l <= r:

            mid = (l+r) // 2

            if nums[mid] >= start: l = mid + 1
            elif (nums[mid] < start) and nums[mid-1] >= start: return nums[mid]
            elif nums[mid] < start: r = mid - 1

        return start


class TestFindMin(unittest.TestCase):

    def test_single_element_list(self):
        s = Solution()
        self.assertEqual(s.findMin([1]), 1)

    def test_sorted_list(self):
        s = Solution()
        self.assertEqual(s.findMin([1, 2, 3, 4, 5]), 1)

    def test_rotated_list(self):
        s = Solution()
        self.assertEqual(s.findMin([4, 5, 6, 7, 0, 1, 2]), 0)

    def test_rotated_list_with_duplicates(self):
        s = Solution()
        self.assertEqual(s.findMin([2, 2, 2, 0, 1, 2]), 0)

    def test_rotated_list_with_all_duplicates(self):
        s = Solution()
        self.assertEqual(s.findMin([2, 2, 2, 2, 2, 2]), 2)

if __name__ == '__main__':
    unittest.main()
