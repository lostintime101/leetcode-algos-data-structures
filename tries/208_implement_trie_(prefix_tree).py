import unittest

"""

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. 
There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.

"""

class TrieNode:

    def __init__(self):
        self.children = {}
        self.isWordEnd = False


class Trie:

    def __init__(self):
        self.start = TrieNode()

    def insert(self, word: str) -> None:

        curr = self.start

        for let in word:
            if let not in curr.children:
                curr.children[let] = TrieNode()
            curr = curr.children[let]

        curr.isWordEnd = True

    def search(self, word: str) -> bool:

        curr = self.start

        for let in word:
            if let not in curr.children: return False
            curr = curr.children[let]
        return curr.isWordEnd

    def startsWith(self, prefix: str) -> bool:

        curr = self.start

        for let in prefix:
            if let not in curr.children: return False
            curr = curr.children[let]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

import unittest


class TestTrie(unittest.TestCase):

    def setUp(self):
        self.trie = Trie()

    def test_insert(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("apple"))  # Exact word match
        self.assertFalse(self.trie.search("app"))  # Partial word match
        self.assertFalse(self.trie.search("apex"))  # No match

        self.trie.insert("banana")
        self.assertTrue(self.trie.search("banana"))
        self.assertFalse(self.trie.search("ban"))  # Partial word match
        self.assertFalse(self.trie.search("band"))  # No match

        self.trie.insert("car")
        self.assertTrue(self.trie.search("car"))
        self.assertFalse(self.trie.search("cat"))  # Partial word match
        self.assertFalse(self.trie.search("care"))  # No match

    def test_starts_with(self):
        self.trie.insert("apple")
        self.trie.insert("banana")
        self.trie.insert("car")

        self.assertTrue(self.trie.startsWith("ap"))  # Prefix match for "apple"
        self.assertTrue(self.trie.startsWith("bana"))  # Partial prefix match for "banana"
        self.assertTrue(self.trie.startsWith("c"))  # Prefix match for "car"
        self.assertFalse(self.trie.startsWith("d"))  # No prefix match

    def test_empty_trie(self):
        self.assertFalse(self.trie.search("apple"))
        self.assertFalse(self.trie.startsWith("a"))


if __name__ == '__main__':
    unittest.main()
