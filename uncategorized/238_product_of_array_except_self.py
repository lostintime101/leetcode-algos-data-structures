
"""

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

"""

class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:

        # BACK AND FORTH O(2n)
        curr, ans = 1, [1]

        for i in range(1, len(nums)):
            ans.append(ans[-1] * nums[i - 1])

        curr = 1
        for j in range(len(nums) - 2, -1, -1):
            curr *= nums[j + 1]
            ans[j] *= curr

        return ans


def run_tests():
    solution = Solution()

    # Test case 1
    nums = [1, 2, 3, 4]
    # The expected output is [24, 12, 8, 6]
    assert solution.productExceptSelf(nums) == [24, 12, 8, 6]

    # Test case 2
    nums = [5, 7, 2, 4]
    # The expected output is [56, 40, 140, 70]
    assert solution.productExceptSelf(nums) == [56, 40, 140, 70]

    # Test case 3
    nums = [3, 1, 6, 2]
    # The expected output is [12, 36, 6, 18]
    assert solution.productExceptSelf(nums) == [12, 36, 6, 18]

    # Test case 5: Single element
    nums = [8]
    # The expected output is [1]
    assert solution.productExceptSelf(nums) == [1]

    print("All tests passed!")


run_tests()

