import unittest
from typing import List

"""

A sequence of numbers is called arithmetic if it consists of at least two elements, and the difference between every two consecutive elements is the same. More formally, a sequence s is arithmetic if and only if s[i+1] - s[i] == s[1] - s[0] for all valid i.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic:

1, 1, 2, 5, 7
You are given an array of n integers, nums, and two arrays of m integers each, l and r, representing the m range queries, where the ith query is the range [l[i], r[i]]. All the arrays are 0-indexed.

Return a list of boolean elements answer, where answer[i] is true if the subarray nums[l[i]], nums[l[i]+1], ... , nums[r[i]] can be rearranged to form an arithmetic sequence, and false otherwise.

Constraints:

n == nums.length
m == l.length
m == r.length
2 <= n <= 500
1 <= m <= 500
0 <= l[i] < r[i] < n
-105 <= nums[i] <= 105

"""

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        ans = []
        for i in range(len(l)):

            new = sorted(nums[l[i]: (r[i] + 1)])
            curr_diff, flag = 0, True

            for j in range(1, len(new)):
                diff = new[j] - new[j - 1]
                print(diff)
                if j == 1:
                    curr_diff = diff
                else:
                    if diff != curr_diff:
                        flag = False
            ans.append(flag)

        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_checkArithmeticSubarrays_single_sequence(self):
        nums = [1, 2, 3, 4, 5]
        l = [0]
        r = [4]
        result = self.solution.checkArithmeticSubarrays(nums, l, r)
        self.assertTrue(result[0])

    def test_checkArithmeticSubarrays_arithmetic_sequence(self):
        nums = [1, 3, 5, 7, 9]
        l = [0]
        r = [4]
        result = self.solution.checkArithmeticSubarrays(nums, l, r)
        self.assertTrue(result[0])

    def test_checkArithmeticSubarrays_non_arithmetic_sequence(self):
        nums = [1, 2, 3, 4, 6]
        l = [0]
        r = [4]
        result = self.solution.checkArithmeticSubarrays(nums, l, r)
        self.assertFalse(result[0])

    def test_checkArithmeticSubarrays_multiple_sequences(self):
        nums = [1, 2, 3, 4, 5, 10, 15, 20]
        l = [0, 5]
        r = [4, 7]
        result = self.solution.checkArithmeticSubarrays(nums, l, r)
        self.assertTrue(result[0])
        self.assertTrue(result[1])


if __name__ == '__main__':
    unittest.main()
