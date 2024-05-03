
import unittest

"""
Given two version numbers, version1 and version2, compare them.

Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.

To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

Return the following:

Constraints:

1 <= version1.length, version2.length <= 500
version1 and version2 only contain digits and '.'.
version1 and version2 are valid version numbers.
All the given revisions in version1 and version2 can be stored in a 32-bit integer.

"""

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        v1 = [int(num) for num in version1.split('.')]
        v2 = [int(num) for num in version2.split('.')]

        while len(v1) > len(v2):
            v2.append(0)
        while len(v2) > len(v1):
            v1.append(0)

        for i in range(len(v1)):
            if v1[i] > v2[i]:
                return 1
            if v1[i] < v2[i]:
                return -1

        return 0


class TestCompareVersion(unittest.TestCase):
    def test_compare_version_equal(self):
        sol = Solution()
        self.assertEqual(sol.compareVersion("1.0", "1.0"), 0)
        self.assertEqual(sol.compareVersion("1.2.3", "1.2.3"), 0)
        self.assertEqual(sol.compareVersion("0.0.1", "0.0.1"), 0)

    def test_compare_version_v1_greater(self):
        sol = Solution()
        self.assertEqual(sol.compareVersion("1.1", "1.0"), 1)
        self.assertEqual(sol.compareVersion("2.0", "1.1"), 1)
        self.assertEqual(sol.compareVersion("1.2.3", "1.2.2"), 1)
        self.assertEqual(sol.compareVersion("1.2.0", "1.1"), 1)

    def test_compare_version_v2_greater(self):
        sol = Solution()
        self.assertEqual(sol.compareVersion("1.0", "1.1"), -1)
        self.assertEqual(sol.compareVersion("1.1", "2.0"), -1)
        self.assertEqual(sol.compareVersion("1.2.2", "1.2.3"), -1)
        self.assertEqual(sol.compareVersion("1.1", "1.2.0"), -1)

    def test_compare_version_different_length(self):
        sol = Solution()
        self.assertEqual(sol.compareVersion("1", "1.0"), 0)
        self.assertEqual(sol.compareVersion("1", "1.1"), -1)
        self.assertEqual(sol.compareVersion("1.0", "1"), 0)
        self.assertEqual(sol.compareVersion("1.1", "1"), 1)


if __name__ == '__main__':
    unittest.main()
