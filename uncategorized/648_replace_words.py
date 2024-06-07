import unittest
from typing import List

"""

In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

Constraints:

1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 100
dictionary[i] consists of only lower-case letters.
1 <= sentence.length <= 106
sentence consists of only lower-case letters and spaces.
The number of words in sentence is in the range [1, 1000]
The length of each word in sentence is in the range [1, 1000]
Every two consecutive words in sentence will be separated by exactly one space.
sentence does not have leading or trailing spaces.

"""

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        d = {}

        for word in dictionary:
            d[word] = True

        ans = []
        sentence_new = sentence.split(" ")

        for word in sentence_new:

            new_word = ""

            found = False
            for l in word:
                new_word += l
                if new_word in d:
                    ans.append(new_word)
                    found = True
                    break

            if not found:
                ans.append(new_word)

        return " ".join(ans)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_replace_words_basic(self):
        dictionary = ["cat", "bat", "rat"]
        sentence = "the cattle was rattled by the battery"
        expected = "the cat was rat by the bat"
        result = self.solution.replaceWords(dictionary, sentence)
        self.assertEqual(result, expected)

    def test_replace_words_no_replacements(self):
        dictionary = ["xyz"]
        sentence = "the cattle was rattled by the battery"
        expected = "the cattle was rattled by the battery"
        result = self.solution.replaceWords(dictionary, sentence)
        self.assertEqual(result, expected)

    def test_replace_words_empty_dictionary(self):
        dictionary = []
        sentence = "the cattle was rattled by the battery"
        expected = "the cattle was rattled by the battery"
        result = self.solution.replaceWords(dictionary, sentence)
        self.assertEqual(result, expected)

    def test_replace_words_empty_sentence(self):
        dictionary = ["cat", "bat", "rat"]
        sentence = ""
        expected = ""
        result = self.solution.replaceWords(dictionary, sentence)
        self.assertEqual(result, expected)

    def test_replace_words_full_match(self):
        dictionary = ["a", "aa", "aaa", "aaaa"]
        sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
        expected = "a a a a a a a a bbb baba a"
        result = self.solution.replaceWords(dictionary, sentence)
        self.assertEqual(result, expected)

    def test_replace_words_multiple_matches(self):
        dictionary = ["cat", "cattle"]
        sentence = "the cattle was rattled by the cat"
        expected = "the cat was rattled by the cat"
        result = self.solution.replaceWords(dictionary, sentence)
        self.assertEqual(result, expected)

    def test_replace_words_partial_match(self):
        dictionary = ["ca", "bat", "rat"]
        sentence = "the cattle was rattled by the battery"
        expected = "the ca was rat by the bat"
        result = self.solution.replaceWords(dictionary, sentence)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
