import unittest


class Solution:
    def lemonadeChange(self, bills: [int]) -> bool:

        change_box = {"$5": 0, "$10": 0, "$20": 0}

        for bill in bills:

            if bill == 5:
                change_box["$5"] += 1

            if bill == 10:
                change_box["$10"] += 1
                change_box["$5"] -= 1

            if bill == 20:
                change_box["$20"] += 1
                if change_box["$10"]:
                    change_box["$10"] -= 1
                    change_box["$5"] -= 1
                else:
                    change_box["$5"] -= 3

            if (change_box["$5"] < 0) or (change_box["$10"] < 0): return False

        return True


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        self.assertEqual(s.lemonadeChange([5,5,5,10,20]), True)

    def test_2(self):
        s = Solution()
        self.assertEqual(s.lemonadeChange([5,5,10]), True)

    def test_3(self):
        s = Solution()
        self.assertEqual(s.lemonadeChange([10,10]), False)

    def test_4(self):
        s = Solution()
        self.assertEqual(s.lemonadeChange([5,5,10,10,20]), False)

if __name__ == '__main__':
    unittest.main()
