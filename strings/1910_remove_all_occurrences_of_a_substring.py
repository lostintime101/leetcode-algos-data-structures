import unittest
from collections import deque

"""

Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:

Find the leftmost occurrence of the substring part and remove it from s.
Return s after removing all occurrences of part.

A substring is a contiguous sequence of characters in a string.

Constraints:

1 <= s.length <= 1000
1 <= part.length <= 1000
s and part consists of lowercase English letters.

"""

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:

        l = len(part)
        s = deque(s)
        found = True

        while found == True:

            found = False

            for i in range(len(s)):

                if (s[i] == part[0]) and (i + l <= len(s)):

                    new_part = ""

                    for j in range(l):
                        new_part += s[i + j]
                        if new_part != part[:j + 1]: break

                    if new_part == part:
                        found = True
                        for _ in range(l):
                            del s[i]
                            break

        return "".join(s)