import unittest

"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

"""

class Solution:
    def letterCombinations(self, digits: str) -> [str]:

        # DFS
        if not digits: return []
        pad = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        ret, i = [], 0

        def dfs(i, let):

            if i == len(digits):
                ret.append(let[::])
                return

            for v in pad[digits[i]]:
                let += v
                i += 1
                dfs(i, let)
                i -= 1
                let = let[:-1]

        dfs(i, "")

        return ret

        # ORIGINAL SOLUTION BFS
        # if digits == "": return None

        # pad = {
        #     2: ["a", "b", "c"],
        #     3: ["d", "e", "f"],
        #     4: ["g", "h", "i"],
        #     5: ["j", "k", "l"],
        #     6: ["m", "n", "o"],
        #     7: ["p", "q", "r", "s"],
        #     8: ["t", "u", "v"],
        #     9: ["w", "x", "y", "z"]
        # }

        # ans = [""]

        # for digit in digits:

        #     num = int(digit)
        #     layer = pad[num]

        #     new_ans = []

        #     for i in range(len(ans)):
        #         for j in range(len(layer)):
        #             new_ans.append(ans[i] + layer[j])

        #     ans = new_ans

        # return ans


class SolutionTests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_letterCombinations_empty_digits(self):
        digits = ""
        expected = []
        result = self.solution.letterCombinations(digits)
        self.assertEqual(result, expected)

    def test_letterCombinations_single_digit(self):
        digits = "2"
        expected = ["a", "b", "c"]
        result = self.solution.letterCombinations(digits)
        self.assertEqual(result, expected)

    def test_letterCombinations_multiple_digits(self):
        digits = "23"
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        result = self.solution.letterCombinations(digits)
        self.assertEqual(result, expected)

    def test_letterCombinations_repeated_digit(self):
        digits = "22"
        expected = ["aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"]
        result = self.solution.letterCombinations(digits)
        self.assertEqual(result, expected)

    def test_letterCombinations_digits_with_zeros(self):
        digits = "23"
        expected = ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
        result = self.solution.letterCombinations(digits)
        self.assertEqual(result, expected)

    def test_letterCombinations_large_input(self):
        digits = "789"
        expected = [
            "ptw", "ptx", "pty", "ptz", "puw", "pux", "puy", "puz", "pvw",
            "pvx", "pvy", "pvz", "qtw", "qtx", "qty", "qtz", "quw", "qux",
            "quy", "quz", "qvw", "qvx", "qvy", "qvz", "rtw", "rtx", "rty",
            "rtz", "ruw", "rux", "ruy", "ruz", "rvw", "rvx", "rvy", "rvz",
            "stw", "stx", "sty", "stz", "suw", "sux", "suy", "suz", "svw",
            "svx", "svy", "svz"
        ]
        result = self.solution.letterCombinations(digits)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()


