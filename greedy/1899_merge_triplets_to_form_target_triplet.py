"""

A triplet is an array of three integers. You are given a 2D integer array triplets,
where triplets[i] = [ai, bi, ci] describes the ith triplet.
You are also given an integer array target = [x, y, z] that describes the triplet you want to obtain.

To obtain target, you may apply the following operation on triplets any number of times (possibly zero):

Choose two indices (0-indexed) i and j (i != j) and update triplets[j] to become [max(ai, aj), max(bi, bj), max(ci, cj)].
For example, if triplets[i] = [2, 5, 3] and triplets[j] = [1, 7, 5], triplets[j]
will be updated to [max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5].
Return true if it is possible to obtain the target triplet [x, y, z] as an element of triplets, or false otherwise.

Constraints:

1 <= triplets.length <= 105
triplets[i].length == target.length == 3
1 <= ai, bi, ci, x, y, z <= 1000

"""

class Solution:
    def mergeTriplets(self, triplets: [[int]], target: [int]) -> bool:

        # GREEDY
        curr = [0,0,0]

        for triplet in triplets:

            local = [max(triplet[0], curr[0]), max(triplet[1], curr[1]), max(triplet[2], curr[2])]

            if (local[0] <= target[0]) and (local[1] <= target[1]) and (local[2] <= target[2]):
                curr = local

            if curr == target: return True

        return False


def test_mergeTriplets():
    solution = Solution()

    # Test case 1
    triplets = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    target = [2, 2, 2]
    expected_output = True
    assert solution.mergeTriplets(triplets, target) == expected_output

    # Test case 2
    triplets = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    target = [3, 4, 5]
    expected_output = True
    assert solution.mergeTriplets(triplets, target) == expected_output

    # Test case 3
    triplets = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    target = [4, 4, 4]
    expected_output = False
    assert solution.mergeTriplets(triplets, target) == expected_output

    # Test case 4 (empty triplets)
    triplets = []
    target = [1, 1, 1]
    expected_output = False
    assert solution.mergeTriplets(triplets, target) == expected_output

    # Test case 5 (single triplet)
    triplets = [[1, 1, 1]]
    target = [1, 1, 1]
    expected_output = True
    assert solution.mergeTriplets(triplets, target) == expected_output

    print("All test cases passed.")


test_mergeTriplets()
