class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i: [] for i in range(n)}
        for x, y in edges:
            adjList[x].append(y)
            adjList[y].append(x)

        visited = set()

        def traverse(start):
            if start in visited:
                return
            visited.add(start)
            for x in adjList[start]:
                traverse(x)

        count = 0
        for x in range(n):
            if x not in visited:
                traverse(x)
                count += 1

        return count

        #O(E+V) as adjlist for E and then dfs on V
        #O(E+V) for space as adjlist(E) and visited(V) sizes
