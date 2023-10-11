import unittest
from typing import List
from collections import defaultdict

"""

You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi] means the ith flower will be in full bloom from starti to endi (inclusive). You are also given a 0-indexed integer array people of size n, where people[i] is the time that the ith person will arrive to see the flowers.

Return an integer array answer of size n, where answer[i] is the number of flowers that are in full bloom when the ith person arrives.

Constraints:

1 <= flowers.length <= 5 * 104
flowers[i].length == 2
1 <= starti <= endi <= 109
1 <= people.length <= 5 * 104
1 <= people[i] <= 109

"""


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:

        starts, stops = [], []

        for flower in flowers:
            starts.append(flower[0])
            stops.append(flower[1])

        starts, stops = sorted(starts), sorted(stops)
        ans, curr = [], 0
        cache = defaultdict(int)

        for person in people:

            if person in cache:
                ans.append(cache[person])
                continue

            l, r = 0, len(starts) - 1

            while l <= r:

                mid = (l + r) // 2

                if starts[mid] == person:
                    while (mid + 1 < len(starts)) and (starts[mid + 1] == person):
                        mid += 1
                    curr += mid + 1
                    break
                elif (starts[mid] < person) and ((mid == len(starts) - 1) or (starts[mid + 1] > person)):
                    curr += mid + 1
                    break
                elif (starts[mid] > person) and ((mid == 0) or (starts[mid - 1] < person)):
                    curr += mid
                    break

                if starts[mid] < person:
                    l = mid + 1
                elif starts[mid] > person:
                    r = mid - 1

            ans.append(curr)
            cache[person] = curr
            curr = 0

        curr = 0
        ans2 = []
        cache2 = defaultdict(int)

        for person in people:

            person -= 1

            if person in cache2:
                ans2.append(cache2[person])
                continue

            l, r = 0, len(starts) - 1

            while l <= r:
                mid = (l + r) // 2

                if stops[mid] == person:
                    while (mid + 1 < len(stops)) and (stops[mid + 1] == person):
                        mid += 1
                    curr += mid + 1
                    break
                elif (stops[mid] < person) and ((mid == len(stops) - 1) or (stops[mid + 1] > person)):
                    curr += mid + 1
                    break
                elif (stops[mid] > person) and ((mid == 0) or (stops[mid - 1] < person)):
                    curr += mid
                    break

                if stops[mid] < person:
                    l = mid + 1
                elif stops[mid] > person:
                    r = mid - 1

            ans2.append(curr)
            cache2[person] = curr
            curr = 0

        for i in range(len(ans)):
            ans[i] -= ans2[i]

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        flowers = [[1, 5], [4, 10], [6, 12]]
        people = [3, 7, 11]
        expected_output = [1, 2, 1]
        self.assertEqual(self.solution.fullBloomFlowers(flowers, people), expected_output)

    def test_case_2(self):
        flowers = [[1, 5], [4, 10], [6, 12]]
        people = [2, 6, 8]
        expected_output = [1, 2, 2]
        self.assertEqual(self.solution.fullBloomFlowers(flowers, people), expected_output)

    def test_case_3(self):
        flowers = [[1, 5], [6, 10], [11, 15]]
        people = [3, 7, 12]
        expected_output = [1, 1, 1]
        self.assertEqual(self.solution.fullBloomFlowers(flowers, people), expected_output)

if __name__ == "__main__":
    unittest.main()
