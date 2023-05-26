import unittest
from typing import List

"""

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.

"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # SIMILAR TO PREVIOUS BUT REVERSED SO USING APPEND NOT INSERT
        digits = digits[::-1]
        for i in range(len(digits)):
            if digits[i] < 9:
                digits[i] += 1
                return digits[::-1]
            else:
                digits[i] = 0
        digits.append(1)
        return digits[::-1]

        # ITERATE FROM BACK CHECKING FOR 9'S
        # for i in range(len(digits)-1, -1, -1):
        #     if digits[i] == 9:
        #         digits[i] = 0
        #     else:
        #         digits[i] += 1
        #         break
        #     if i == 0: digits.insert(0,1)

        # return digits

        # CASTING METHOD
        # ans = int("".join([str(num)for num in digits])) + 1
        # return [int(num) for num in str(ans)]

import unittest

class Solution:
    def plusOne(self, digits):
        digits = digits[::-1]
        for i in range(len(digits)):
            if digits[i] < 9:
                digits[i] += 1
                return digits[::-1]
            else:
                digits[i] = 0
        digits.append(1)
        return digits[::-1]


class SolutionTestCase(unittest.TestCase):
    def test_plusOne(self):
        solution = Solution()

        # Test case: [1, 2, 3]
        digits = [1, 2, 3]
        expected = [1, 2, 4]
        self.assertEqual(solution.plusOne(digits), expected)

        # Test case: [9, 9, 9]
        digits = [9, 9, 9]
        expected = [1, 0, 0, 0]
        self.assertEqual(solution.plusOne(digits), expected)

        # Test case: [0]
        digits = [0]
        expected = [1]
        self.assertEqual(solution.plusOne(digits), expected)


if __name__ == '__main__':
    unittest.main()
