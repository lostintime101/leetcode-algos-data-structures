import unittest

class Solution:

    def minimumTotal(self, triangle):

        # row 1
        if len(triangle) == 1: return triangle[0][0]

        # row 2
        triangle[1][0] += triangle[0][0]
        triangle[1][1] += triangle[0][0]
        if len(triangle) == 2: return min(triangle[1])

        prev = triangle[1]

        # rows 3 and below
        for row in range(2, len(triangle)):

            curr = triangle[row]

            curr[0] += prev[0]

            # print(prev, curr)
            for i in range(1, len(curr) - 1):
                curr[i] += min(prev[i - 1], prev[i])

            curr[-1] += prev[-1]

            prev = curr

        return min(curr)


class TestSolution(unittest.TestCase):

    def test_minimumTotal(self):
        solution = Solution()

        # Test case 1
        triangle = [[2]]
        self.assertEqual(solution.minimumTotal(triangle), 2)

        # Test case 2
        triangle = [[2], [3, 4]]
        self.assertEqual(solution.minimumTotal(triangle), 5)

        # Test case 3
        triangle = [[2], [3, 4], [6, 5, 7]]
        self.assertEqual(solution.minimumTotal(triangle), 10)

        # Test case 4
        triangle = [[-10]]
        self.assertEqual(solution.minimumTotal(triangle), -10)

        # Test case 5
        triangle = [[-10], [1, -3]]
        self.assertEqual(solution.minimumTotal(triangle), -13)

        # Test case 6
        triangle = [[-1], [2, 3], [1, -1, -3]]
        self.assertEqual(solution.minimumTotal(triangle), -1)

if __name__ == '__main__':
    unittest.main()

