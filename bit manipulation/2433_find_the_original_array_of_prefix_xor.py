import unittest
from typing import List

"""

You are given an integer array pref of size n. Find and return the array arr of size n that satisfies:

pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
Note that ^ denotes the bitwise-xor operation.

It can be proven that the answer is unique.

Constraints:

1 <= pref.length <= 105
0 <= pref[i] <= 106

"""

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = pref[::]

        for i in range(1, len(pref)):
            ans[i] = pref[i - 1] ^ pref[i]

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_findArray(self):
        # Test case 1
        pref1 = [1, 2, 3, 4, 5]
        expected_output1 = [1, 3, 1, 7, 1]
        self.assertEqual(self.solution.findArray(pref1), expected_output1)

        # Test case 2
        pref2 = [0, 0, 0, 0, 0]
        expected_output2 = [0, 0, 0, 0, 0]
        self.assertEqual(self.solution.findArray(pref2), expected_output2)

        # Test case 3
        pref3 = [1, 3, 5, 7, 9]
        expected_output3 = [1, 2, 6, 2, 14]
        self.assertEqual(self.solution.findArray(pref3), expected_output3)


if __name__ == "__main__":
    unittest.main()
