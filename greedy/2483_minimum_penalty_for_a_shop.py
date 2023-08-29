import unittest


"""

You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':

if the ith character is 'Y', it means that customers come at the ith hour
whereas 'N' indicates that no customers come at the ith hour.
If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:

For every hour when the shop is open and no customers come, the penalty increases by 1.
For every hour when the shop is closed and customers come, the penalty increases by 1.
Return the earliest hour at which the shop must be closed to incur a minimum penalty.

Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.

Constraints:

1 <= customers.length <= 105
customers consists only of characters 'Y' and 'N'.

"""


class Solution:
    def bestClosingTime(self, customers: str) -> int:

        second = sum([1 for customer in customers if customer == "Y"])
        first = ans = 0
        min_penalty = first + second

        for i in range(len(customers)):

            if customers[i] == "N":
                first += 1
            else:
                second -= 1

            if first + second < min_penalty:
                ans = i + 1
                min_penalty = first + second

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        customers = "YYNYYY"
        expected_result = 6
        self.assertEqual(self.solution.bestClosingTime(customers), expected_result)

    def test_case_2(self):
        customers = "NNNN"
        expected_result = 0
        self.assertEqual(self.solution.bestClosingTime(customers), expected_result)

    def test_case_3(self):
        customers = "YYYYN"
        expected_result = 4
        self.assertEqual(self.solution.bestClosingTime(customers), expected_result)

    def test_case_4(self):
        customers = "YNYNYNYN"
        expected_result = 1
        self.assertEqual(self.solution.bestClosingTime(customers), expected_result)

    def test_case_5(self):
        customers = "NYYNNY"
        expected_result = 3
        self.assertEqual(self.solution.bestClosingTime(customers), expected_result)


if __name__ == '__main__':
    unittest.main()
