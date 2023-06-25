import unittest
from typing import List
from collections import defaultdict
import random

"""

Given an integer array nums with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the array nums.
int pick(int target) Picks a random index i from nums where nums[i] == target. If there are multiple valid i's, then each index should have an equal probability of returning.

Constraints:

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
target is an integer from nums.
At most 104 calls will be made to pick.

"""

class Solution:

    def __init__(self, nums: List[int]):
        self.hash_map = defaultdict(list)

        for i, v in enumerate(nums): self.hash_map[v].append(i)

    def pick(self, target: int) -> int:
        random_int = random.randint(0, len(self.hash_map[target]) - 1)

        return self.hash_map[target][random_int]

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)