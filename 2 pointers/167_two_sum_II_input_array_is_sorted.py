import unittest

"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

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
    def twoSum(self, numbers: [int], target: int) -> [int]:

        l = 0
        r = len(numbers) - 1

        while l <= r:

            ans = numbers[l] + numbers[r]

            if ans == target:
                return [l + 1, r + 1]
            elif ans > target:
                r -= 1
            elif ans < target:
                l += 1

        # BINARY SEARCH
        # for i in range(len(numbers)):

        #     left = 0
        #     right = len(numbers)-1

        #     while left <= right:

        #         mid = (left + right) //2

        #         total = numbers[mid] + numbers[i]

        #         if total == target:

        #             if i == mid: return [i+1, mid+2]

        #             return [i+1, mid+1]

        #         elif total > target: right = mid -1

        #         else: left = mid +1


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        numbers = [2, 7, 11, 15]
        target = 9
        expected = [1, 2]
        self.assertEqual(self.solution.twoSum(numbers, target), expected)

    def test_2(self):
        numbers = [2, 3, 4]
        target = 6
        expected = [1, 3]
        self.assertEqual(self.solution.twoSum(numbers, target), expected)

    def test_3(self):
        numbers = [-1, 0]
        target = -1
        expected = [1, 2]
        self.assertEqual(self.solution.twoSum(numbers, target), expected)

    def test_4(self):
        numbers = [0, 0, 3, 4]
        target = 0
        expected = [1, 2]
        self.assertEqual(self.solution.twoSum(numbers, target), expected)

    def test_5(self):
        numbers = [5, 25, 50]
        target = 75
        expected = [2, 3]
        self.assertEqual(self.solution.twoSum(numbers, target), expected)

    def test_6(self):
        numbers = [1, 2, 3, 4, 5]
        target = 7
        expected = [2, 5]
        self.assertEqual(self.solution.twoSum(numbers, target), expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
