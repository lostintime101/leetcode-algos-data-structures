import unittest
from typing import List
from collections import defaultdict

"""

Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

Constraints:

n == nums.length
1 <= n <= 16
nums[i].length == n
nums[i] is either '0' or '1'.
All the strings of nums are unique.

"""

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        hash_map = defaultdict(bool)
        for num in nums: hash_map[num] = True

        n = len(nums[0])

        for i in range(2 ** n):

            base = list(str(bin(i)[2:]))
            front = ['0'] * (n - len(base))
            front += base
            front = "".join(front)

            if hash_map[front] == False: return front


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_findDifferentBinaryString(self):
        # Test case 1
        nums1 = ["00", "01"]
        self.assertEqual(self.solution.findDifferentBinaryString(nums1), "10")

        # Test case 2
        nums2 = ["01", "10"]
        self.assertEqual(self.solution.findDifferentBinaryString(nums2), "00")

        # Test case 3
        nums3 = ["111", "011", "001"]
        self.assertEqual(self.solution.findDifferentBinaryString(nums3), "000")

        # Add more test cases as needed


if __name__ == '__main__':
    unittest.main()
