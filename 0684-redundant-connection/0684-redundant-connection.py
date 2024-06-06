class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [x for x in range(1001)]
        ans = []

        def findParent(node):
            while parent[node] != node:
                node = parent[node]
            return node

        def union(x, y):
            parentx = findParent(x)
            parenty = findParent(y)

            if parentx != parenty:
                parent[parentx] = parenty
            else:
                ans.append(x)
                ans.append(y)

        for source, dest in edges:
            union(source, dest)

        return ans
