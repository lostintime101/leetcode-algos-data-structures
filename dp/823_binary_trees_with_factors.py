from typing import List
import unittest

"""

Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.

Constraints:

1 <= arr.length <= 1000
2 <= arr[i] <= 109
All the values of arr are unique.

"""

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:

        MOD = 10 ** 9 + 7
        arr = sorted(arr)
        dp = {arr[0]: 1}
        ans = 1

        for i in range(1, len(arr)):

            r = i - 1
            l = 0
            new_ans = 1

            while l <= r:

                curr = arr[i] / arr[l]

                if curr == arr[r]:
                    if arr[l] == arr[r]:
                        new_ans += (dp[arr[l]] * dp[arr[r]])
                    else:
                        new_ans += (dp[arr[l]] * dp[arr[r]]) * 2
                    l += 1
                if curr > arr[r]:
                    l += 1
                    r += 1

                r -= 1
            dp[arr[i]] = new_ans
            ans += new_ans

        return ans % MOD


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_element(self):
        self.assertEqual(self.solution.numFactoredBinaryTrees([2]), 1)

    def test_no_possible_trees(self):
        self.assertEqual(self.solution.numFactoredBinaryTrees([1, 3]), 2)

    def test_example_case(self):
        self.assertEqual(self.solution.numFactoredBinaryTrees([2, 4]), 3)

    def test_large_numbers(self):
        self.assertEqual(self.solution.numFactoredBinaryTrees([18, 3, 6, 2]), 12)

    def test_duplicate_elements(self):
        self.assertEqual(self.solution.numFactoredBinaryTrees([2, 2, 4]), 4)

    def test_prime_numbers(self):
        self.assertEqual(self.solution.numFactoredBinaryTrees([7, 11, 13]), 3)


if __name__ == "__main__":
    unittest.main()
