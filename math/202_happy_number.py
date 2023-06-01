import unittest

"""

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Constraints:

1 <= n <= 231 - 1

"""

class Solution:
    def isHappy(self, n: int) -> bool:

        # MODULO SOLUTION

        seen = set()
        while True:

            n = self.sumOfSquares(n)

            if n == 1: return True
            if n in seen: return False

            seen.add(n)

    def sumOfSquares(self, num: int) -> int:
        ans = 0
        while num:
            ans += num % 10
            num = num // 10
        return ans

        # CASTING SOLUTION
        # loops = 0
        # while True:

        #     num_list = [int(num)**2 for num in str(n)]

        #     total = 0

        #     for i in num_list:

        #         total += i
        #     if total == 1:
        #         return True
        #     else:
        #         n = total
        #         loops += 1

        #         if loops > 20:
        #             return False


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_isHappy(self):
        # Test case 1
        n1 = 19
        self.assertTrue(self.solution.isHappy(n1))

        # Test case 2
        n2 = 2
        self.assertFalse(self.solution.isHappy(n2))

        # Test case 5
        n5 = 0
        self.assertFalse(self.solution.isHappy(n5))

if __name__ == '__main__':
    unittest.main()
