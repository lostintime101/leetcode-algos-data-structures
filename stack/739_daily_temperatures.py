import unittest

"""
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait after the ith day
to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100

"""

class Solution:
    def dailyTemperatures(self, temperatures: [int]) -> [int]:

        MAXTEMP = 100
        MINTEMP = 30

        ret = [0 for i in temperatures]
        temps = [[] for temp in range(MINTEMP, MAXTEMP + 1)]

        for i, v in enumerate(temperatures):

            temps[v - MINTEMP].append(i)
            lower = temps[:v - MINTEMP]

            for j in range(len(lower)):

                if lower[j]:

                    for k in lower[j]:
                        ret[k] = i - k

                    temps[j] = []

        return ret


class TestSolution(unittest.TestCase):

    def test_dailyTemperatures(self):
        solution = Solution()

        # Test case 1
        temps1 = [73, 74, 75, 71, 69, 72, 76, 73]
        expected1 = [1, 1, 4, 2, 1, 1, 0, 0]
        self.assertEqual(solution.dailyTemperatures(temps1), expected1)

        # Test case 2
        temps2 = [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
        expected2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
        self.assertEqual(solution.dailyTemperatures(temps2), expected2)

        # Test case 3
        temps3 = [100, 90, 80, 70, 60, 50, 40, 30]
        expected3 = [0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(solution.dailyTemperatures(temps3), expected3)

        # Test case 4
        temps4 = [100, 100, 100, 100, 100]
        expected4 = [0, 0, 0, 0, 0]
        self.assertEqual(solution.dailyTemperatures(temps4), expected4)


if __name__ == '__main__':
    unittest.main()
