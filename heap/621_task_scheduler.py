import unittest
from typing import List
from collections import Counter, deque
from heapq import heappop, heappush


"""

Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task
Tasks could be done in any order. Each task is done in one unit of time. 
For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks 
(the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

Constraints:

1 <= task.length <= 104
tasks[i] is upper-case English letter.
The integer n is in the range [0, 100].

"""


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # HEAP + QUEUE

        count = Counter(tasks)
        heap = []

        for i, v in count.items():
            heappush(heap, -v)

        time = 0
        queue = deque()

        while heap or queue:

            time += 1

            if heap:
                cnt = 1 + heappop(heap)
                if cnt: queue.append([time + n, cnt])

            if queue and queue[0][0] == time:
                heappush(heap, queue.popleft()[1])

        return time



class SolutionTests(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_leastInterval_example1(self):
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 2
        expected = 8
        actual = self.solution.leastInterval(tasks, n)
        self.assertEqual(actual, expected)

    def test_leastInterval_example2(self):
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 0
        expected = 6
        actual = self.solution.leastInterval(tasks, n)
        self.assertEqual(actual, expected)

    def test_leastInterval_example3(self):
        tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
        n = 2
        expected = 16
        actual = self.solution.leastInterval(tasks, n)
        self.assertEqual(actual, expected)

    def test_leastInterval_single_task(self):
        tasks = ["A"]
        n = 2
        expected = 1
        actual = self.solution.leastInterval(tasks, n)
        self.assertEqual(actual, expected)

    def test_leastInterval_no_idle_time(self):
        tasks = ["A", "B", "C", "D"]
        n = 0
        expected = 4
        actual = self.solution.leastInterval(tasks, n)
        self.assertEqual(actual, expected)

    def test_leastInterval_empty_tasks(self):
        tasks = []
        n = 3
        expected = 0
        actual = self.solution.leastInterval(tasks, n)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
