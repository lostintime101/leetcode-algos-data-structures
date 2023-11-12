import unittest
from typing import List
from collections import defaultdict


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        if source == target: return 0

        stops = defaultdict(set)
        prev, curr, final = set(), set(), set()

        for i, route in enumerate(routes):
            for stop in route:
                stops[stop].add(i)
                if stop == source: prev.add(i)
                if stop == target: final.add(i)

        count = 1
        seen = defaultdict(bool)

        for stop in stops[target]:
            if stop in stops[source]: return 1

        while prev:

            for route in prev:

                for stop in routes[route]:

                    if not seen[stop]:

                        for rou in stops[stop]:
                            if rou in final: return count + 1
                            curr.add(rou)

                        seen[stop] = True

            prev = curr
            curr = set()
            count += 1

        return -1

