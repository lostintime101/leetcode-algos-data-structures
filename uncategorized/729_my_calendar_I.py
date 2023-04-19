import unittest

"""

You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a 
double booking. 

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval 
[start, end), the range of real numbers x such that start <= x < end. 

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object. boolean book(int start, int end) Returns true if the event can be added 
to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to 
the calendar. 

Constraints:

0 <= start < end <= 109
At most 1000 calls will be made to book.

"""


class MyCalendar:

    def __init__(self):

        self.calendar = []

    def book(self, start: int, end: int) -> bool:

        for session in self.calendar:

            if session[0] <= start < session[1]:
                return False

            if session[0] < end <= session[1]:
                return False

            if (start <= session[0]) and (end >= session[1]):
                return False

        self.calendar.append([start, end])

        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)


class TestMyCalendar(unittest.TestCase):
    def setUp(self):
        self.calendar = MyCalendar()

    def test_book(self):
        # First booking
        self.assertTrue(self.calendar.book(10, 20))

        # Booking within an existing session
        self.assertFalse(self.calendar.book(15, 18))

        # Booking that starts during an existing session
        self.assertFalse(self.calendar.book(5, 15))

        # Booking that ends during an existing session
        self.assertFalse(self.calendar.book(15, 25))

        # Booking that starts and ends outside of existing sessions
        self.assertTrue(self.calendar.book(25, 30))

        # Booking that starts before and ends during an existing session
        self.assertFalse(self.calendar.book(5, 12))

        # Booking that starts during and ends after an existing session
        self.assertFalse(self.calendar.book(15, 30))


if __name__ == '__main__':
    unittest.main()
