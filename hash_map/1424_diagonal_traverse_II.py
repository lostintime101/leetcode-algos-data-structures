import unittest
from typing import List
from collections import defaultdict

"""

Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.

Constraints:

1 <= nums.length <= 105
1 <= nums[i].length <= 105
1 <= sum(nums[i].length) <= 105
1 <= nums[i][j] <= 105

"""


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:

        mapping = defaultdict(list)

        for r, row in enumerate(nums):
            for c, val in enumerate(row):
                mapping[r + c].append(val)

        ans = []
        count = 0
        while count in mapping:
            ans.extend(mapping[count][::-1])
            count += 1

        return ans

        # # BFS Solution
        # prev, curr = [(0,0)], []
        # ans = []

        # seen = defaultdict(bool)
        # while prev:

        #     for p in prev:

        #         r, c = p[0], p[1]
        #         print(r,c)
        #         ans.append(nums[r][c])
        #         if r+1 <= len(nums)-1 and c <= len(nums[r+1])-1 and not seen[(r+1, c)]:
        #             curr.append((r+1, c))
        #             seen[(r+1,c)] = True

        #         if r <= len(nums)-1 and c+1 <= len(nums[r])-1 and not seen[(r, c+1)]:
        #             curr.append((r, c+1))
        #             seen[(r,c+1)] = True

        #     prev = curr
        #     curr = []

        # return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_findDiagonalOrder(self):
        # Test Case 1
        nums1 = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual(self.solution.findDiagonalOrder(nums1), [1, 4, 2, 7, 5, 3, 8, 6, 9])

        # Test Case 2
        nums2 = [
            [1, 2],
            [3, 4],
            [5, 6]
        ]
        self.assertEqual(self.solution.findDiagonalOrder(nums2), [1, 3, 2, 5, 4, 6])



if __name__ == '__main__':
    unittest.main()
