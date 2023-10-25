import unittest

"""

We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

Constraints:

1 <= n <= 30
1 <= k <= 2n - 1

"""

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        # 1 0 1
        # 2 01 2
        # 3 01 10 4
        # 4 0110 1001 8
        # 5 01101001 10010110 16  10 - 0

        def backtrack(n, k, true_false):

            if n == 1:
                if true_false:
                    return 0
                else:
                    return 1

            half = 2 ** (n - 2)

            if k > half:
                k -= half
                if true_false:
                    true_false = False
                else:
                    true_false = True

            return backtrack(n - 1, k, true_false)

        return backtrack(n, k, True)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_kthGrammar(self):
        self.assertEqual(self.solution.kthGrammar(1, 1), 0)
        self.assertEqual(self.solution.kthGrammar(2, 1), 0)
        self.assertEqual(self.solution.kthGrammar(2, 2), 1)
        self.assertEqual(self.solution.kthGrammar(3, 3), 1)
        self.assertEqual(self.solution.kthGrammar(4, 5), 1)
        self.assertEqual(self.solution.kthGrammar(5, 10), 0)
        # Add more test cases as needed


if __name__ == "__main__":
    unittest.main()
