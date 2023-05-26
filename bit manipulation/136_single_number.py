import unittest

"""

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.


"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # BIT MANIPULATION
        ans = nums[0]
        for i in range(1, len(nums)):
            ans = ans ^ nums[i]
        return ans

        # HASHMAP VERSION
        # seen = {}
        # for num in nums:
        #     if num not in seen: seen[num] = True
        #     else: del seen[num]
        # return seen.keys()[0]

        # ORIGINAL SOLUTION
        # for num in nums:
        #     if nums.count(num) < 2:
        #         return num

class Solution(object):
    def singleNumber(self, nums):
        ans = nums[0]
        for i in range(1, len(nums)):
            ans = ans ^ nums[i]
        return ans


class SolutionTestCase(unittest.TestCase):
    def test_singleNumber(self):
        solution = Solution()

        # Test case: [2, 2, 1]
        nums = [2, 2, 1]
        expected = 1
        self.assertEqual(solution.singleNumber(nums), expected)

        # Test case: [4, 1, 2, 1, 2]
        nums = [4, 1, 2, 1, 2]
        expected = 4
        self.assertEqual(solution.singleNumber(nums), expected)

if __name__ == '__main__':
    unittest.main()