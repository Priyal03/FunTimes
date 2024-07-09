class Solution:
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))

        def union(self, x, y):
            rootx = self.find(x)
            rooty = self.find(y)
            if rootx != rooty:
                self.parent[rootx] = rooty

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = self.UnionFind(n + 1)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    uf.union(i, j)

        parents = set()
        for x in range(len(isConnected)):
            parents.add(uf.find(x))

        return len(parents)
