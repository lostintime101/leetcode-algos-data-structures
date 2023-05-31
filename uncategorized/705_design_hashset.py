
import unittest

"""

Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

Constraints:

0 <= key <= 106
At most 104 calls will be made to add, remove, and contains.

"""

class MyHashSet:

    def __init__(self):
        self.hashset = {}

    def add(self, key: int) -> None:
        self.hashset[key] = 0

    def remove(self, key: int) -> None:
        if key in self.hashset:
            del self.hashset[key]

    def contains(self, key: int) -> bool:
        if key in self.hashset: return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


class TestMyHashSet(unittest.TestCase):
    def setUp(self):
        self.hashset = MyHashSet()

    def test_add(self):
        self.hashset.add(1)
        self.assertTrue(self.hashset.contains(1))

    def test_remove(self):
        self.hashset.add(2)
        self.hashset.remove(2)
        self.assertFalse(self.hashset.contains(2))

    def test_contains(self):
        self.hashset.add(3)
        self.assertTrue(self.hashset.contains(3))
        self.assertFalse(self.hashset.contains(4))

if __name__ == "__main__":
    unittest.main()
