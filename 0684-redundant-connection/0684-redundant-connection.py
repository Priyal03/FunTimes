class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        ans = []

        def union(x, y) -> bool:

            rootx = find(x)
            rooty = find(y)
            if rootx == rooty:
                return False
            else:
                parent[rootx] = rooty
                return True

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for i, j in edges:
            if not union(i, j):
                ans = [i, j]

        return ans
