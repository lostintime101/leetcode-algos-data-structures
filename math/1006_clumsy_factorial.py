import unittest

"""

The factorial of a positive integer n is the product of all positive integers less than or equal to n.

For example, factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1.
We make a clumsy factorial using the integers in decreasing order by swapping out the multiply operations for a fixed rotation of operations with multiply '*', divide '/', add '+', and subtract '-' in this order.

For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.
However, these operations are still applied using the usual order of operations of arithmetic. We do all multiplication and division steps before any addition or subtraction steps, and multiplication and division steps are processed left to right.

Additionally, the division that we use is floor division such that 10 * 9 / 8 = 90 / 8 = 11.

Given an integer n, return the clumsy factorial of n.

Constraints:

1 <= n <= 104

"""

class Solution:
    def clumsy(self, n: int) -> int:
        # * // + - order
        operators = ["*", "//", "+", "-"]

        ret = str(n)

        for i in range(1, n):
            num = n - i
            op = operators[(i - 1) % 4]
            ret += op + str(num)

        return eval(ret)



class TestSolution(unittest.TestCase):

    def test_clumsy(self):
        solution = Solution()

        # Test case 1
        n = 4
        expected = 7  # 4 * 3 // 2 + 1 = 7
        self.assertEqual(solution.clumsy(n), expected)

        # Test case 2
        n = 10
        expected = 12  # 10 * 9 // 8 + 7 - 6 * 5 // 4 + 3 - 2 * 1 = 12
        self.assertEqual(solution.clumsy(n), expected)

        # Test case 3
        n = 1
        expected = 1  # Only one number, so the result is the same as the input
        self.assertEqual(solution.clumsy(n), expected)

        # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
