import unittest
from heapq import heappush, heappop

"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

Constraints:
1 <= k <= 104
0 <= nums.length <= 104
-104 <= nums[i] <= 104
-104 <= val <= 104
At most 104 calls will be made to add.
It is guaranteed that there will be at least k elements in the array when you search for the kth element.

"""

class KthLargest:

    def __init__(self, k: int, nums: [int]):

        # sort nums and only store relevant part (i.e. last k values)
        self.heap = sorted(nums)[-k:]
        self.k = k

    def add(self, val: int) -> int:

        # edge case
        if len(self.heap) < self.k:
            heappush(self.heap, val)

        # reorder heap only if val bigger than smallest heap value
        elif val > self.heap[0]:
            heappush(self.heap, val)
            heappop(self.heap)

        # return smallest val in heap
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


class KthLargestTests(unittest.TestCase):
    def setUp(self):
        self.k = 3
        self.nums = [4, 5, 8, 2]
        self.kth_largest = KthLargest(self.k, self.nums)

    def test_add(self):
        result = self.kth_largest.add(3)
        self.assertEqual(result, 4, "Incorrect result for test case 1")

        result = self.kth_largest.add(5)
        self.assertEqual(result, 5, "Incorrect result for test case 2")

        result = self.kth_largest.add(10)
        self.assertEqual(result, 5, "Incorrect result for test case 3")

        result = self.kth_largest.add(9)
        self.assertEqual(result, 8, "Incorrect result for test case 4")

        result = self.kth_largest.add(4)
        self.assertEqual(result, 8, "Incorrect result for test case 5")

if __name__ == "__main__":
    unittest.main()
