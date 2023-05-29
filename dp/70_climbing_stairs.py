import unittest

"""

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Constraints:

1 <= n <= 45

"""

class Solution:
    def climbStairs(self, n: int) -> int:

        prev, curr = 1, 2
        if n == 1: return prev
        if n == 2: return curr

        for _ in range(n - 2):
            temp = curr
            curr = prev + curr
            prev = temp

        return curr

        # # RECURSIVE DFS - TIMES OUT

        # ret = [0]
        # def dfs(curr):

        #     if curr == n:
        #         ret[0] += 1
        #         return
        #     if curr > n: return

        #     return dfs(curr+1) or dfs(curr+2)

        # dfs(0)
        # return ret[0]


import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_climbStairs_n1(self):
        result = self.solution.climbStairs(1)
        self.assertEqual(result, 1)

    def test_climbStairs_n2(self):
        result = self.solution.climbStairs(2)
        self.assertEqual(result, 2)

    def test_climbStairs_n3(self):
        result = self.solution.climbStairs(3)
        self.assertEqual(result, 3)

    def test_climbStairs_n4(self):
        result = self.solution.climbStairs(4)
        self.assertEqual(result, 5)

    def test_climbStairs_n5(self):
        result = self.solution.climbStairs(5)
        self.assertEqual(result, 8)

    def test_climbStairs_n10(self):
        result = self.solution.climbStairs(10)
        self.assertEqual(result, 89)

    def test_climbStairs_n15(self):
        result = self.solution.climbStairs(15)
        self.assertEqual(result, 987)

if __name__ == '__main__':
    unittest.main()
