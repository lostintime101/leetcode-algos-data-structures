import unittest
from typing import List

"""

A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.

Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level i.e. time[i] * satisfaction[i].

Return the maximum sum of like-time coefficient that the chef can obtain after dishes preparation.

Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.

Constraints:

n == satisfaction.length
1 <= n <= 500
-1000 <= satisfaction[i] <= 1000

"""

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        satisfaction.sort()
        ret = 0

        while satisfaction:

            sat = 0
            for i,v in enumerate(satisfaction):
                sat += (i+1)*v
            ret = max(ret, sat)
            satisfaction = satisfaction[1:]

        return ret



def test_maxSatisfaction():
    solution = Solution()

    # Test case 1
    satisfaction1 = [-1, -8, 0, 5, -9]
    assert solution.maxSatisfaction(satisfaction1) == 14

    # Test case 2
    satisfaction2 = [4, 3, 2]
    assert solution.maxSatisfaction(satisfaction2) == 20

    # Test case 3
    satisfaction3 = [-1, -4, -5]
    assert solution.maxSatisfaction(satisfaction3) == 0

    # Test case 4
    satisfaction4 = [-2, 5, -1, 0, 3, -3]
    assert solution.maxSatisfaction(satisfaction4) == 35

    # Test case 5
    satisfaction5 = [-1, -2, -3, -4, -5]
    assert solution.maxSatisfaction(satisfaction5) == 0

    print("All test cases pass")

test_maxSatisfaction()
