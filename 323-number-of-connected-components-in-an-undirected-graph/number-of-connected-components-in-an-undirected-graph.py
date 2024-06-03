class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # if len(edges) > (n - 1):
        #     return 1
        parent = [num for num in range(n)]
        count = 0

        def findParent(x):
            # find the root parent
            while x != parent[x]:
                x = parent[x]
            return x

        def union(x, y):
            parentx = findParent(x)
            parenty = findParent(y)
            if parentx != parenty:
                parent[parenty] = parentx

        for start, end in edges:
            union(start, end)

        # count number of roots
        for i in range(n):
            if i == parent[i]:
                count += 1

        return count
