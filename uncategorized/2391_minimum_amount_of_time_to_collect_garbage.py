import unittest
from typing import List
from collections import Counter

"""

You are given a 0-indexed array of strings garbage where garbage[i] represents the assortment of garbage at the ith house. garbage[i] consists only of the characters 'M', 'P' and 'G' representing one unit of metal, paper and glass garbage respectively. Picking up one unit of any type of garbage takes 1 minute.

You are also given a 0-indexed integer array travel where travel[i] is the number of minutes needed to go from house i to house i + 1.

There are three garbage trucks in the city, each responsible for picking up one type of garbage. Each garbage truck starts at house 0 and must visit each house in order; however, they do not need to visit every house.

Only one garbage truck may be used at any given moment. While one truck is driving or picking up garbage, the other two trucks cannot do anything.

Return the minimum number of minutes needed to pick up all the garbage.

Constraints:

2 <= garbage.length <= 105
garbage[i] consists of only the letters 'M', 'P', and 'G'.
1 <= garbage[i].length <= 10
travel.length == garbage.length - 1
1 <= travel[i] <= 100 

"""

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:

        metal, paper, glass = 0, 0, 0
        last_seen = {"M": 0, "P": 0, "G": 0}
        travel_totals = [0] * len(garbage)
        curr_travel = 0

        for i, v in enumerate(garbage):

            if i != 0:
                curr_travel += travel[i - 1]
                travel_totals[i] = curr_travel

            freq = Counter(v)

            if "M" in freq:
                metal += freq["M"]
                last_seen["M"] = i
            if "P" in freq:
                metal += freq["P"]
                last_seen["P"] = i
            if "G" in freq:
                metal += freq["G"]
                last_seen["G"] = i

        metal += travel_totals[last_seen["M"]]
        paper += travel_totals[last_seen["P"]]
        glass += travel_totals[last_seen["G"]]

        return metal + paper + glass


class TestSolution(unittest.TestCase):

    def setUp(self):
        # Initialize any common setup needed for the tests
        pass

    def test_garbageCollection(self):
        solution = Solution()

        # Test case 1
        garbage = ["M", "P", "G"]
        travel = [1, 2, 3]
        result = solution.garbageCollection(garbage, travel)
        self.assertEqual(result, 7)

        # Test case 2
        garbage = ["M", "P", "G", "M", "P", "G"]
        travel = [1, 2, 3, 1, 2, 3]
        result = solution.garbageCollection(garbage, travel)
        self.assertEqual(result, 28)

        # Add more test cases as needed

    def tearDown(self):
        # Clean up resources if needed
        pass


if __name__ == '__main__':
    unittest.main()
