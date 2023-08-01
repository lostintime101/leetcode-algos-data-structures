from typing import List
import unittest

"""

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

Constraints:

1 <= n <= 20
1 <= k <= n

"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        # CLASSIC BACKTRACT WORKS WELL
        ans = []

        def backtrack(index, state):
            # print(index, state)

            if len(state) == k:
                ans.append(state)
                return
            if index > n: return

            for i in range(index + 1, n + 1):
                state.append(i)
                backtrack(i, state[::])
                state.pop()

        backtrack(0, [])

        return ans

        # ALSO WORKS BUT CACHE DOESN'T HELP, CASTING BACK AND FORTH CREATES EXTRA WORK
        # ans = []

        # @cache
        # def backtrack(index, state):

        #     if len(state) == k:
        #         ans.append(list(state))
        #         return
        #     if index > n: return

        #     for i in range(index+1,n+1):
        #         backtrack(i, tuple(list(state) + [i]))

        # backtrack(0, tuple())

        # return ans


# Create a Test class that inherits from unittest.TestCase
class TestSolution(unittest.TestCase):
    def test_combine(self):
        solution = Solution()

        # Test Case 1
        n1, k1 = 4, 2
        expected_output1 = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
        self.assertEqual(solution.combine(n1, k1), expected_output1)

        # Test Case 2
        n2, k2 = 5, 3
        expected_output2 = [
            [1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5],
            [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5]
        ]
        self.assertEqual(solution.combine(n2, k2), expected_output2)

        # Test Case 3: Empty output for k > n
        n3, k3 = 3, 4
        expected_output3 = []
        self.assertEqual(solution.combine(n3, k3), expected_output3)

        # Add more test cases as needed


if __name__ == "__main__":
    unittest.main()


