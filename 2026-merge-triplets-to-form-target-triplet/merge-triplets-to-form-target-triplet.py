class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        a = b = c = 0

        for row in triplets:

            if row[0] > target[0] or row[1] > target[1] or row[2] > target[2]:
                continue

            a = max(a, row[0])
            b = max(b, row[1])
            c = max(c, row[2])

            if a == target[0] and b == target[1] and c == target[2]:
                return True

        return False
