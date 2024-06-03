class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjmatrix = {node: [] for node in range(n)}
        count = 0
        for x, y in edges:
            adjmatrix[x].append(y)
            adjmatrix[y].append(x)

        visited = set()

        def dfs(node):
            visited.add(node)
            for neighbor in adjmatrix[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        for x in range(n):
            if x not in visited:
                dfs(x)
                count += 1

        return count
