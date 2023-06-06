import unittest
from typing import List

"""

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.


"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # SIMPLE SOLUTION - 2 POINTERS

        left, right = 0, len(numbers) - 1

        while left <= right:

            curr = numbers[left] + numbers[right]

            if curr == target:
                return [left + 1, right + 1]

            elif curr > target:
                right -= 1

            else:
                left += 1

        # WORKS BUT TOO LONG

        # for i in range(len(numbers)-1):

        #     left, right = i, len(numbers)-1

        #     if i and numbers[i] == numbers[i-1]: continue
        #     while numbers[right] == numbers [right-1]: right -= 1

        #     while left < right:

        #         curr = numbers[left] + numbers[right]

        #         if curr == target: return [left+1, right+1]

        #         elif curr > target: right -= 1

        #         else: break

        # return [left+1, right+2]


class TwoSumTests(unittest.TestCase):
    def test_twoSum(self):
        solution = Solution()


        numbers = [2, 7, 11, 15]
        target = 9
        expected_output = [1, 2]
        self.assertEqual(solution.twoSum(numbers, target), expected_output)

if __name__ == '__main__':
    unittest.main()
