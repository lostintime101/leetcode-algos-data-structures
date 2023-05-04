import unittest

"""
Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105

"""
class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:

        ans = []
        nums = sorted(nums)

        for i, v in enumerate(nums):

            if i > 0 and v == nums[i - 1]: continue

            l, r = i + 1, len(nums) - 1
            target = 0 - v

            while l < r:

                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1

                else:
                    ans.append([v, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r: l += 1

        return ans

        # BRUTE FORCE WITH 3 POINTERS - TIMES OUT

        # nums = sorted(nums)
        # l, c, r = 0, 1, len(nums)-1
        # ans = []

        # while l <= len(nums)-3:

        #     while c <= len(nums)-2:

        #         while r > c:

        #             if (nums[l] + nums[c] + nums[r]) == 0:

        #                 ans.append(sorted([nums[l], nums[c], nums[r]]))
        #                 break

        #             r -= 1

        #         c += 1
        #         r = len(nums)-1

        #     l += 1
        #     c = l+1
        #     r = len(nums)-1

        # new_ans = []
        # for i in ans:
        #     if i not in new_ans: new_ans.append(i)

        # return new_ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_example_1(self):
        nums = [-1, 0, 1, 2, -1, -4]
        expected_output = [[-1, -1, 2], [-1, 0, 1]]
        self.assertCountEqual(self.s.threeSum(nums), expected_output)

    def test_example_2(self):
        nums = []
        expected_output = []
        self.assertCountEqual(self.s.threeSum(nums), expected_output)

    def test_example_3(self):
        nums = [0]
        expected_output = []
        self.assertCountEqual(self.s.threeSum(nums), expected_output)

    def test_custom_1(self):
        nums = [1, 2, 3, 4, 5]
        expected_output = []
        self.assertCountEqual(self.s.threeSum(nums), expected_output)

    def test_custom_2(self):
        nums = [0, 0, 0, 0, 0]
        expected_output = [[0, 0, 0]]
        self.assertCountEqual(self.s.threeSum(nums), expected_output)

    def test_custom_3(self):
        nums = [3, 0, -2, -1, 1, 2]
        expected_output = [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
        self.assertCountEqual(self.s.threeSum(nums), expected_output)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
