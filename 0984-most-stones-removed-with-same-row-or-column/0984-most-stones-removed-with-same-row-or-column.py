class Solution:
    # n - number of connected maxRemovals
    def removeStones(self, stones: List[List[int]]) -> int:

        parent = {}
        n = len(stones)

        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            if rootx != rooty:
                parent[rootx] = rooty
                return 1
            return 0

        def find(x):
            if x not in parent:
                parent[x] = x
                return x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        maxRemovals = 0

        def isSameRowCol(x, y):
            return x[0] == y[0] or x[1] == y[1]

        for i in range(n):
            for j in range(i + 1, n):
                if isSameRowCol(stones[i], stones[j]):
                    maxRemovals += union(i, j)

        return maxRemovals