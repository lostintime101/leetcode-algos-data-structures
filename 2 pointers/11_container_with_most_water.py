import unittest

"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

class Solution:
    def maxArea(self, height) -> int:

        # BRUTE FORCE O(n^2)

        # ret = 0

        # for i,start in enumerate(height):

        #     for dist, end in enumerate(height[i+1:]):

        #         area = (dist+1) * min(start, end)
        #         print(area)

        #         if area > ret: ret = area

        # return ret

        # 2 POINTERS O(n)

        ret = 0
        l = 0
        r = len(height) - 1

        while l < r:

            area = (r - l) * min(height[l], height[r])

            if ret < area: ret = area

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return ret


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_maxArea(self):
        self.assertEqual(self.solution.maxArea([1,8,6,2,5,4,8,3,7]), 49)
        self.assertEqual(self.solution.maxArea([1,1]), 1)
        self.assertEqual(self.solution.maxArea([4,3,2,1,4]), 16)
        self.assertEqual(self.solution.maxArea([1,2,1]), 2)
        self.assertEqual(self.solution.maxArea([2,3,4,5,18,17,6]), 17)
        self.assertEqual(self.solution.maxArea([2,3,10,5,7,8,9]), 36)


if __name__ == '__main__':
    unittest.main()
