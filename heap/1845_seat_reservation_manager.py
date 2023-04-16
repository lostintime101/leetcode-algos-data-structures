import unittest
import heapq


class SeatManager:

    def __init__(self, n: int):
        self.available_seats = [num for num in range(1, n + 1)]  # [1,2,3...n]

    def reserve(self) -> int:
        return heapq.heappop(self.available_seats)

        # BINARY TREE SOLUTION (VALID, BUT SLOW)
        # new_reservation = self.available_seats[0]
        # self.available_seats.pop(0)
        # print(self.available_seats, new_reservation)
        # return new_reservation

    def unreserve(self, seatNumber: int) -> None:
        return heapq.heappush(self.available_seats, seatNumber)

        # BINARY TREE SOLUTION
        # length = len(self.available_seats)
        # if length == 0:
        #     self.available_seats.append(seatNumber)
        #     return

        # left = 0
        # right = min(length-1, seatNumber-1)

        # while left <= right:

        #     mid = (left + right) // 2

        #     if (self.available_seats[mid] < seatNumber) and (self.available_seats[mid]+1 > seatNumber):
        #         self.available_seats.insert(mid+1, seatNumber)
        #         return

        #     elif self.available_seats[mid] > seatNumber:
        #         right = mid-1

        #     elif self.available_seats[mid] < seatNumber:
        #         left = mid+1

        # self.available_seats.insert(mid, seatNumber)
        # return

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)


class TestSeatManager(unittest.TestCase):

    def test_1(self):
        sm = SeatManager(5)
        self.assertEqual(sm.reserve(), 1)
        self.assertEqual(sm.reserve(), 2)
        sm.unreserve(1)
        self.assertEqual(sm.reserve(), 1)

    def test_2(self):
        sm = SeatManager(10)
        for i in range(10):
            self.assertEqual(sm.reserve(), i+1)
        sm.unreserve(5)
        sm.unreserve(2)
        self.assertEqual(sm.reserve(), 2)
        self.assertEqual(sm.reserve(), 5)

    def test_3(self):
        sm = SeatManager(3)
        self.assertEqual(sm.reserve(), 1)
        self.assertEqual(sm.reserve(), 2)
        self.assertEqual(sm.reserve(), 3)
        self.assertRaises(IndexError, sm.reserve)

    def test_4(self):
        sm = SeatManager(1)
        self.assertEqual(sm.reserve(), 1)
        self.assertRaises(IndexError, sm.reserve)


if __name__ == '__main__':
    unittest.main()
